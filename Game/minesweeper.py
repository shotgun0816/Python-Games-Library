from pathlib import Path
import pygame, os
import tkinter as tk
from pygame import mixer
import random

board=[["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
       ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],]

white=(255, 255, 255)
light_red=(255, 75 ,75)

def run_game(parent, root):
    for row in board:
        row[:] = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    parent.configure(width=600, height=600)
    parent.pack_propagate(False)
    parent.update_idletasks()
    parent.focus_set()

    pygame.init()
    game_screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Minesweeper")

    mixer.init()
    dir_path=Path(os.path.dirname(__file__)).parent / "Audio"
    victory=dir_path/"crowd_small_chil_ec049202_9klCwI6.mp3"
    loser=dir_path/"roblox-explosion-sound.mp3"
    victory_audio=pygame.mixer.Sound(victory)
    loser_audio=pygame.mixer.Sound(loser)

    game_running=True
    after_id=None
    game_over=False
    game_lose=False
    safe=216
    revealed = [[False for _ in range(16)] for _ in range(16)]
    exploded_cell = None
    result_font=pygame.font.Font(None, 72)
    result_text=None
    directions=[(-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1)]

    def plant_bombs():
        for _ in range(1, 40):
            plant=False
            while plant==False:
                row=random.randint(0, 15)
                column=random.randint(0, 15)
                if board[row][column]=="":
                    board[row][column]="X"
                    plant=True
                else:
                    plant=False

    def count_bombs(check_y, check_x):
        bomb_count=0

        for x_count, y_count in directions:
            check_row=check_y+y_count
            check_column=check_x+x_count
            if 0 <= check_row < 16 and 0 <= check_column < 16:
                if board[check_row][check_column]=="X":
                    bomb_count+=1
        return bomb_count

    def reveal(y, x):
        nonlocal exploded_cell, game_over, game_lose, safe
        if not (0<=x<16 and 0<=y<16):
            return
        if revealed[y][x]:
            return
        if board[y][x]=="X":
            game_over=True
            game_lose=True
            exploded_cell = (y, x)
            finish_game()
            return
    
        revealed[y][x]=True
        safe-=1
        if safe == 0:
            game_over=True
            finish_game()
            return
        if count_bombs(y, x)==0:
            for dy, dx in directions:
                reveal(y+dy, x+dx)


    def handle_events(event):
        if event.type==pygame.QUIT:
            stop_game()
        elif event.type==pygame.MOUSEBUTTONDOWN and not game_over:
            column=int(event.pos[0]//37.5)
            row=int(event.pos[1]//37.5)
            reveal(row, column)

    def draw_lines():
        block=600/16
        for line in range(17):
            position=round(line * block)
            pygame.draw.line(game_screen, white, (position, 0), (position, 600))
            pygame.draw.line(game_screen, white, (0, position), (600, position))

    def draw_board():
        font = pygame.font.SysFont(None, 30)
        game_screen.fill("grey")
        draw_lines()

        for y in range(16):
            for x in range(16):
                if exploded_cell == (y, x):
                    rect = pygame.Rect(x * 37.5, y * 37.5, 37.5, 37.5)
                    pygame.draw.rect(game_screen, light_red, rect)
                elif revealed[y][x]:
                    rect = pygame.Rect(x * 37.5, y * 37.5, 37.5, 37.5)
                    pygame.draw.rect(game_screen, "lightgrey", rect)

                    bomb_count = count_bombs(y, x)
                    if bomb_count > 0:
                        text = font.render(str(bomb_count), True, "black")
                        rect2 = text.get_rect(center=(x * 37.5 + 18.75, y * 37.5 + 18.75))
                        game_screen.blit(text, rect2)

    def finish_game():
        nonlocal result_text
        if game_over==True and game_lose==True:
            loser_audio.play()
            result_text=result_font.render("You Lose", True, "red")
        elif game_over==True and safe==0:
            victory_audio.play()
            result_text=result_font.render("You Win", True, "green")

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            handle_events(event)

        draw_board()
        if result_text is not None:
            result_rect = result_text.get_rect(center=(300, 300))
            game_screen.blit(result_text, result_rect)
        pygame.display.flip()
        after_id=root.after(16, game_loop)

    def stop_game():
        nonlocal game_running
        game_running=False
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()

    plant_bombs()
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