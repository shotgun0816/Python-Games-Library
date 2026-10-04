import os, pygame, random, sys
from pathlib import Path
from pygame import mixer
import tkinter as tk

light_red=(255, 75, 75)

def run_game(parent, root):
    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    parent.configure(width=700, height=400)
    parent.pack_propagate(False)
    parent.update_idletasks()
    parent.focus_set()

    pygame.init()
    game_screen=pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Type Practice")

    mixer.init()
    dir_path=Path(os.path.dirname(__file__)).parent/"Audio"
    countdown=dir_path/"u_edtmwfwu7c-beep-329314.mp3"
    wrong=dir_path/"wrong-answer-sound-effect.mp3"
    victory=dir_path/"crowd_small_chil_ec049202_9klCwI6.mp3"
    countdown_audio=pygame.mixer.Sound(countdown)
    wrong_audio=pygame.mixer.Sound(wrong)
    victory_audio=pygame.mixer.Sound(victory)

    font=pygame.font.Font(None, 28)
    result_font=pygame.font.Font(None, 56)
    result_text=None
    letter_count=None
    characters=None
    chosen_line=None
    game_running=True
    letter_num=None
    user_input=""
    game_over=False
    after_id=None
    wpm=None
    time_used=None
    start_time=None

    def get_file():
        nonlocal chosen_line, letter_count, characters, letter_num
        dir_file=Path(os.path.dirname(__file__)).parent/"Others"
        file=dir_file/"paragraphs.txt"
        file_items=open(file, "r", encoding="utf-8")
        lines=file_items.readlines()
        chosen_line=random.choice(lines).strip()

        characters=list(chosen_line)
        letter_num=len(characters)

    def time_delay():
        nonlocal time_left
        time_left-=1
        if time_left>0:
            countdown_audio.play()
            root.after(1000, time_delay)

    def draw_game():
        game_screen.fill((30, 30, 30))

        left = 20
        right = game_screen.get_width() - 20
        x = left
        y = 30
        line_height = font.get_linesize()
        for index, character in enumerate(chosen_line):
            if character == "\n":
                x = left
                y += line_height
                continue

            char_width = font.size(character)[0]
            if x > left and x + char_width > right:
                x = left
                y += line_height

            color = (100, 220, 120) if index < len(user_input) else (220, 220, 220)
            char_surface = font.render(character, True, color)
            game_screen.blit(char_surface, (x, y))
            x += char_width

        if result_text is not None:
            result_rect = result_text.get_rect(
                center=(game_screen.get_width() // 2, game_screen.get_height() - 80)
            )
            game_screen.blit(result_text, result_rect)

        pygame.display.flip()

    def game_loop():
        nonlocal after_id
        if not game_running:
            return
        for event in pygame.event.get():
            handle_events(event)

            if not game_running:
                return
            
        draw_game()
        after_id=root.after(16, game_loop)

    def handle_events(event):
        if event.type == pygame.QUIT:
            stop_game()

    def handle_keys(event):
        nonlocal user_input, time_left
        if time_left==0:
            if not game_running:
                return "break"

            if event.keysym in ("Return", "KP_Enter"):
                if len(user_input) == len(characters):
                    finish_game()
            elif event.char and len(user_input) < len(characters):
                if event.char == characters[len(user_input)]:
                    user_input += event.char
                else:
                    wrong_audio.play()

        return "break"

    def finish_game():
        nonlocal game_over, game_running, start_time, time_used, letter_num, wpm, result_text
        game_over=True
        game_running=False
        victory_audio.play()
        time_used=(pygame.time.get_ticks()-start_time)/1000/60
        wpm=(letter_num/5)/time_used
        result_text=result_font.render(f"Your WPM is {wpm:.1f}", True, light_red)
        draw_game()

    def stop_game():
        nonlocal game_running
        game_running=False
        root.unbind("<KeyPress>", key_binding)
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()

    get_file()
    time_left=5
    root.after(1000, time_delay)
    start_time=pygame.time.get_ticks()
    key_binding=root.bind("<KeyPress>", handle_keys, add="+")
    parent.focus_set()
    game_loop()
    return stop_game

if __name__=="__main__":
    root=tk.Tk()
    root.title("Type Practice")
    root.geometry("1200x600")
    game_frame=tk.Frame(root, width=1200, height=600)
    game_frame.pack()
    game_frame.pack_propagate(False)
    root.update_idletasks()
    run_game(game_frame, root)
    root.mainloop()
