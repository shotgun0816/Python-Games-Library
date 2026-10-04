import os, pygame, random, sys
from pathlib import Path
from pygame import mixer
import tkinter as tk

def run_game(parent, root):
    os.environ["SDL_WINDOWID"] = str(parent.winfo_id())

    parent.configure(width=700, height=400)
    parent.pack_propagate(False)
    parent.update_idletasks()
    parent.focus_set()

    pygame.init()
    game_screen=pygame.display.set_mode((700, 400))
    pygame.display.set_caption("Type Practice")

    letter_count=None
    characters=None
    chosen_line=None
    game_running=True
    letter_num=None
    game_over=False
    after_id=None
    wpm=None
    time_used=None

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
        time=5
        time-=1
        if time>0:
            root.after(1000, time_delay)


    def game_loop():
        if game_running==False:
            return

        for event in pygame.event.get():
            handle_events(event)

    def handle_events(event):
        if event.type == pygame.QUIT:
            stop_game()

    def handle_keys(events):
        pass


    def stop_game():
        nonlocal game_running
        game_running=False
        if after_id is not None:
            root.after_cancel(after_id)
        pygame.quit()


    get_file()
    root.after(1000, time_delay)
    key_binding=root.bind("<KeyPress>", handle_keys, add="+")
    game_loop()
    return stop_game

if __name__=="__main__":
    root=tk.Tk()
    root.title("Type Practice")
    root.geometry("1200x600")
    game_frame=tk.Frame(root, width=700, height=400)
    game_frame.pack()
    game_frame.pack_propagate(False)
    root.update_idletasks()
    run_game(game_frame, root)
    root.mainloop()

