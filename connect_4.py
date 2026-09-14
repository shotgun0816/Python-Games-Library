import pygame
import os
import random
from pygame import mixer
from pathlib import Path

board=[["", "", "", "", "", "", ""],
       ["", "", "", "", "", "", ""],
       ["", "", "", "", "", "", ""],
       ["", "", "", "", "", "", ""],
       ["", "", "", "", "", "", ""],
       ["", "", "", "", "", "", ""],]

red=(255, 0, 0)

win=False

def run_game(parent, root):
    for row in board:
        row[:]=["", "", "", "", "", "", ""]

    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())
    
    pygame.init()
    game_screen=pygame.display.set_mode((700,600))
    pygame.display.set_caption("Connect 4")
    mark_font=pygame.font.Font(None, 160)
    result_font=pygame.font.Font(None, 200)
    after_id = None
    game_running = True
    player_turn = True
    game_over = False
    result_text = None

    mixer.init()
    dir_path=Path(os.path.dirname(__file__))
    victory=dir_path/"crowd_small_chil_ec049202_9klCwI6.mp3"
    loser=dir_path/"downer_noise.mp3"
    draw=dir_path/"tung-tung-sahur.mp3"
    victory_audio=pygame.mixer.Sound(victory)
    loser_audio=pygame.mixer.Sound(loser)
    draw_audio=pygame.mixer.Sound(draw)

    def draw_lines():
        pygame.draw.line(game_screen, "white", (0,0), (0,600), width=3)
        pygame.draw.line(game_screen, "white", (700,0), (700,600), width=3)
        pygame.draw.line(game_screen, "white", (0,600), (700,600), width=3)

        pygame.draw.line(game_screen, "white", (0,100), (700,100), width=1)
        pygame.draw.line(game_screen, "white", (0,200), (700,200), width=1)
        pygame.draw.line(game_screen, "white", (0,300), (700,300), width=1)
        pygame.draw.line(game_screen, "white", (0,400), (700,400), width=1)
        pygame.draw.line(game_screen, "white", (0,500), (700,500), width=1)
        pygame.draw.line(game_screen, "white", (0,600), (700,600), width=1)

        pygame.draw.line(game_screen, "white", (100,0), (100,600), width=1)
        pygame.draw.line(game_screen, "white", (200,0), (200,600), width=1)
        pygame.draw.line(game_screen, "white", (300,0), (300,600), width=1)
        pygame.draw.line(game_screen, "white", (400,0), (400,600), width=1)
        pygame.draw.line(game_screen, "white", (500,0), (500,600), width=1)
        pygame.draw.line(game_screen, "white", (600,0), (600,600), width=1)

    def handle_event(event):
        nonlocal player_turn
        if event.type==pygame.QUIT:
            stop_game()
        elif event.type==pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            pos_x=event.pos[0]
            column=pos_x//100
            placed=False
            for y in range(5, -1, -1):
                if board[y][column]=="":
                    board[y][column]="X"
                    placed=True
                    break

            if not placed:
                return

            if check_winner("X"):
                victory_audio.play()
                finish_game("You Win!")
            elif board_full():
                finish_game("Draw")
            else:
                player_turn=False
                root.after(1000, npc_turn)

    def board_full():
        draw_audio.play()
        return all(cell != "" for row in board for cell in row)

    def npc_turn():
        nonlocal player_turn
        valid=False
        if game_over:
            return

        while valid==False:
            column=random.randint(0,6)
            for row in range(5, -1, -1):
                if board[row][column]=="":
                    board[row][column]="O"
                    valid=True
                    break
        

        if check_winner("O"):
            loser_audio.play()
            finish_game("You Lose")
        elif board_full():
            finish_game("Draw")
        else:
            player_turn=True

    def draw_marks():
        for y, row in enumerate(board):
            for x, mark in enumerate(row):
                if mark == "":
                    continue

                color = "red" if mark == "X" else "yellow"
                center = (x * 100 + 50, y * 100 + 50)
                pygame.draw.circle(game_screen, color, center, 40)
    
    def check_winner(mark):
        directions = (
            (1, 0),   # vertical
            (0, 1),   # horizontal
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
        )

        for row in range(6):
            for column in range(7):
                for row_step, column_step in directions:
                    positions = [
                        (
                            row + row_step * offset,
                            column + column_step * offset
                        )
                        for offset in range(4)
                    ]

                    if all(
                        0 <= check_row < 6
                        and 0 <= check_column < 7
                        and board[check_row][check_column] == mark
                        for check_row, check_column in positions
                    ):
                        return True

        return False
        
    def finish_game(message):
        nonlocal game_over, result_text
        game_over = True
        result_text = result_font.render(message, True, red)

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            handle_event(event)
                        
        game_screen.fill("black")
        draw_lines()
        draw_marks()

        if result_text is not None:
            result_rect = result_text.get_rect(center=(350, 300))
            game_screen.blit(result_text, result_rect)

        pygame.display.flip()
        after_id=root.after(16, game_loop)

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