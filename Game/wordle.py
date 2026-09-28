import os, pygame, random, sys
from pathlib import Path
from pygame import mixer
import tkinter as tk
from collections import Counter

green=(0,180, 0)
light_green=(0, 250, 0)
yellow=(255, 218, 94)
light_red=(250, 75, 75)
dark_grey=(100, 100, 100)

board=[["", "", "", "", ""],
       ["", "", "", "", ""],
       ["", "", "", "", ""],
       ["", "", "", "", ""],
       ["", "", "", "", ""],]

guesses=[["", "", "", "", ""],
         ["", "", "", "", ""],
         ["", "", "", "", ""],
         ["", "", "", "", ""],
         ["", "", "", "", ""],]

def run_game(parent, root):
    for row in board:
        row[:]=["", "", "", "", ""]
    for row in guesses:
        row[:]=["", "", "", "", ""]

    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    parent.configure(width=600, height=600)
    parent.pack_propagate(False)
    parent.update_idletasks()
    parent.focus_set()

    pygame.init()
    game_screen=pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Wordle")

    game_running=True
    game_over=False
    result_font=pygame.font.Font(None, 72)
    result_text=None
    after_id=None
    game_win=False
    user_word=""
    word_chosen=None
    chosen_list=None
    chances=5
    line_board=0

    mixer.init()
    dir_path=Path(os.path.dirname(__file__)).parent/"Audio"
    victory=dir_path/"crowd_small_chil_ec049202_9klCwI6.mp3"
    loser=dir_path/"downer_noise.mp3"
    victory_audio=pygame.mixer.Sound(victory)
    loser_audio=pygame.mixer.Sound(loser)
    
    def get_file():
        nonlocal word_chosen, chosen_list
        dir_file=Path(os.path.dirname(__file__)).parent/"Others"
        file=dir_file/"5_words.txt"
        file_items=open(file, "r", encoding="utf-8")
        lines=file_items.readlines()
        word_chosen=random.choice(lines).strip().upper()

        chosen_list=list(word_chosen)

    def draw_board():
        game_screen.fill("grey")
        draw_lines()

        for row_index, row in enumerate(guesses):
            for column, letter in enumerate(row):
                if letter:
                    marker=board[row_index][column]
                    color={"*": green, "!": yellow, "_": dark_grey}.get(marker, "white")
                    draw_letter(letter, column, row_index, color)

        if not game_over:
            for column, letter in enumerate(user_word):
                draw_letter(letter, column, line_board)

    def draw_lines():
        block=600/5
        for line in range(6):
            position=round(line * block)
            pygame.draw.line(game_screen, "white", (position, 0), (position, 600))
            pygame.draw.line(game_screen, "white", (0, position), (600, position))

    def draw_letter(letter, num, row, tile_color="grey"):
        tile = pygame.Rect(num * 120 + 2, row * 120 + 2, 116, 116)
        pygame.draw.rect(game_screen, tile_color, tile)

        font = pygame.font.SysFont(None, 72)
        text = font.render(letter, True, "white")
        position = (num * 120 + 60, row * 120 + 60)
        game_screen.blit(text, text.get_rect(center=position))

    def handle_key(event):
        nonlocal user_word
        if game_over or chances<=0:
            return "break"

        if event.keysym=="BackSpace":
            user_word=user_word[:-1]
        elif event.keysym in ("Return", "KP_Enter"):
            if len(user_word)==5:
                decide_win(user_word)
        elif event.char.isalpha() and len(user_word)<5:
            user_word+=event.char.upper()
        return "break"

    def handle_events(event):
        if event.type==pygame.QUIT:
            stop_game()

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            handle_events(event)

        draw_board()
        if result_text is not None:
            result_rect=result_text.get_rect(center=(300, 300))
            game_screen.blit(result_text, result_rect)

        pygame.display.flip()
        after_id=root.after(16, game_loop)

    def decide_win(word):
        nonlocal game_win, game_over, chances, line_board, user_word
        guesses[line_board][:]=list(word)
        check_word(word)
        if word==word_chosen:
            game_win=True
            game_over=True
            finish_game(True)
        else:
            chances-=1
            if chances==0:
                game_over=True
                finish_game(False)
            else:
                line_board+=1
                user_word=""

    def check_word(word):
        feedback=["_"] * 5
        remaining=Counter()
        for index, letter in enumerate(chosen_list):
            if word[index]==letter:
                feedback[index]="*"
            else:
                remaining[letter]+=1

        for index, letter in enumerate(word):
            if feedback[index]=="_" and remaining[letter]>0:
                feedback[index]="!"
                remaining[letter]-=1

        board[line_board][:]=feedback

    def finish_game(status):
        nonlocal result_text
        if status and game_over:
            victory_audio.play()
            result_text=result_font.render("You Win", True, light_green)
        elif not status and game_over:
            loser_audio.play()
            result_text=result_font.render(f"You Lose, the word is \n{word_chosen}", True, light_red)

    def stop_game():
        nonlocal game_running
        game_running=False
        root.unbind("<KeyPress>", key_binding)
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()

    key_binding=root.bind("<KeyPress>", handle_key, add="+")
    get_file()
    game_loop()
    return stop_game

if __name__=="__main__":
    root=tk.Tk()
    root.title("Minesweeper")
    root.geometry("600x600")
    game_frame=tk.Frame(root, width=600, height=600)
    game_frame.pack()
    game_frame.pack_propagate(False)
    root.update_idletasks()
    run_game(game_frame, root)
    root.mainloop()