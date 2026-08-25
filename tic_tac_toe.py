import pygame
import os
import tkinter.font as tkFont
import tkinter as tk
import time
import random

board=[["", "", ""],
       ["", "", ""],
       ["", "", ""]]

win=False
white = (255, 255, 255)
      
def run_game(parent, root):
    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    pygame.init()
    game_screen=pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic-Tac-Toe")
    after_id = None
    game_running = True

    def draw_lines():
        pygame.draw.line(game_screen, "white", (200, 0), (200, 600), width=1)
        pygame.draw.line(game_screen, "white", (400, 0), (400, 600), width=1)
        pygame.draw.line(game_screen, "white", (0, 400), (600, 400), width=1)
        pygame.draw.line(game_screen, "white", (0, 200), (600, 200), width=1)

        pygame.draw.line(game_screen, "white", (0, 0), (0, 600), width=3)
        pygame.draw.line(game_screen, "white", (600, 0), (600, 600), width=3)
        pygame.draw.line(game_screen, "white", (0, 0), (600, 0), width=3)
        pygame.draw.line(game_screen, "white", (0, 600), (600, 600), width=3)

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            def click():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y=event.pos
                    column=pos_y//200
                    row=pos_x//200
                    if board[row][column] is not "":
                        pass
                    else:
                        board[row][column]="X"
                        
                if event.type==pygame.QUIT:
                    stop_game()
                    return

                time.sleep(2)

            def npc_turn():
                npc_x=random.randint(0, 2)
                npc_y=random.randint(0, 2)
                while board[npc_y][npc_x] is not "":
                    npc_x=random.randint(0, 2)
                    npc_y=random.randint(0, 2)

                board[npc_y][npc_x]=="O"
                time.sleep(1)

            def check_player():
                conditions=[
                    board[0], board[1], board[2],
                    [board[0][0], board[1][0], board[2][0]],
                    [board[0][1], board[1][1], board[2][1]],
                    [board[0][2], board[1][2], board[2][2]],
                    [board[0][0], board[1][1], board[2][2]],
                    [board[0][2], board[1][1], board[2][0]],
                ]
                return any(all(cell=="X" for cell in line) for line in conditions)

            def check_npc():
                conditions=[
                    board[0], board[1], board[2],
                    [board[0][0], board[1][0], board[2][0]],
                    [board[0][1], board[1][1], board[2][1]],
                    [board[0][2], board[1][2], board[2][2]],
                    [board[0][0], board[1][1], board[2][2]],
                    [board[0][2], board[1][1], board[2][0]],
                ]
                return any(all(cell=="O" for cell in line) for line in conditions)
            
            if check_player():
                title_font=pygame.font.Font(None, 48)
                text=title_font.render("You Win", True, white)
                text_box=text.get_rect()
                text_box.center=(600//2, 600//2)
                win=True
                print("You Win")
            elif check_npc():
                text=title_font.render("You Lose", True, white)
                text_box=text.get_rect()
                text_box.center=(600//2, 600//2)
                print("You lose")
                    




        game_screen.fill("black")
        draw_lines()
        pygame.display.flip()
        after_id = root.after(16, game_loop)

    def stop_game():
        nonlocal game_running
        game_running = False
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()

    game_loop()
    return stop_game


if __name__ == "__main__":
    run_game()