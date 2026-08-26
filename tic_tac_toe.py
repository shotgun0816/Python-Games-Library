import pygame
import os
import random
from pygame import mixer
from pathlib import Path

board=[["", "", ""],
       ["", "", ""],
       ["", "", ""]]

win=False
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
11
def run_game(parent, root):
    for row in board:
        row[:] = ["", "", ""]

    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    pygame.init()
    game_screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Tic-Tac-Toe")
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
        pygame.draw.line(game_screen, "white", (200, 0), (200, 600), width=1)
        pygame.draw.line(game_screen, "white", (400, 0), (400, 600), width=1)
        pygame.draw.line(game_screen, "white", (0, 400), (600, 400), width=1)
        pygame.draw.line(game_screen, "white", (0, 200), (600, 200), width=1)

        pygame.draw.line(game_screen, "white", (0, 0), (0, 600), width=3)
        pygame.draw.line(game_screen, "white", (600, 0), (600, 600), width=3)
        pygame.draw.line(game_screen, "white", (0, 0), (600, 0), width=3)
        pygame.draw.line(game_screen, "white", (0, 600), (600, 600), width=3)

    def draw_marks():
        for row in range(3):
            for column in range(3):
                mark=board[row][column]
                if mark:
                    text=mark_font.render(mark, True, white)
                    position=text.get_rect(center=(column * 200 + 100, row * 200 + 100))
                    game_screen.blit(text, position)

    def check_winner(mark):
        lines = board + [
            [board[0][column], board[1][column], board[2][column]]
            for column in range(3)
        ] + [
            [board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]],
        ]
        return any(all(cell == mark for cell in line) for line in lines)

    def board_full():
        return all(cell != "" for row in board for cell in row)

    def finish_game(message):
        nonlocal game_over, result_text
        game_over = True
        result_text = result_font.render(message, True, red)

    def npc_turn():
        nonlocal player_turn
        if game_over:
            return

        empty_cells = [
            (row, column)
            for row in range(3)
            for column in range(3)
            if board[row][column] == ""
        ]
        if not empty_cells:
            return

        row, column = random.choice(empty_cells)
        board[row][column] = "O"
        if check_winner("O"):
            loser_audio.play()
            finish_game("You Lose")
        elif board_full():
            finish_game("Draw")
        else:
            player_turn = True

    def handle_event(event):
        nonlocal player_turn
        if event.type == pygame.QUIT:
            stop_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            pos_x, pos_y = event.pos
            column = pos_x // 200
            row = pos_y // 200
            if board[row][column] == "":
                board[row][column] = "X"
                if check_winner("X"):
                    victory_audio.play()
                    finish_game("You Win")
                    
                elif board_full():
                    draw_audio.play()
                    finish_game("Draw")
                else:
                    player_turn = False
                    root.after(1000, npc_turn)

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            handle_event(event)
                    
        game_screen.fill("black")
        draw_lines()
        draw_marks()
        if result_text:
            result_position=result_text.get_rect(center=(300, 300))
            game_screen.blit(result_text, result_position)
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