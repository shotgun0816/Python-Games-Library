from pathlib import Path
import pygame, os
import tkinter as tk
from pygame import mixer

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

white=(255,255,255)

def run_game(parent, root):
    for row in board:
        row[:]=["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    pygame.init()
    game_screen=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Minesweeper")

    game_running=True
    after_id=None

    def draw_lines():
        block=600/16
        for line in range(17):
            position=round(line * block)
            pygame.draw.line(game_screen, white, (position, 0), (position, 600))
            pygame.draw.line(game_screen, white, (0, position), (600, position))

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        game_screen.fill("black")
        draw_lines()

        pygame.display.flip()
        after_id=root.after(16, game_loop)

    def stop_game():
        nonlocal game_running
        game_running=False
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()

    game_loop()
    return stop_game


if __name__=="__main__":
    root=tk.Tk()
    root.title("Minesweeper")
    game_frame=tk.Frame(root, width=600, height=600)
    game_frame.pack()
    game_frame.pack_propagate(False)
    root.update_idletasks()
    run_game(game_frame, root)
    root.mainloop()