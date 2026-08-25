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

    def game_loop():
        nonlocal after_id
        if not game_running:
            return

        for event in pygame.event.get():
            handle_event(event)
                        
        game_screen.fill("black")
        draw_lines()

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