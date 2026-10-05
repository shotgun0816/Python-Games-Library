import tkinter as tk
from tkinter import *
import tkinter.font as tkFont

from Game import tic_tac_toe as game_1
from Game import connect_4 as game_2
from Game import minesweeper as game_3
from Game import wordle as game_4
from Game import type_practice as game_5

from tkinter import PhotoImage
from tkinter.ttk import *
from pathlib import Path
from PIL import Image, ImageTk

def main():
        root=tk.Tk()
        root.geometry("900x700")
        root.title("Games")
        root.configure(cursor="tcross")
        menu=tk.Frame(root)
        menu.configure(bg="light yellow")
        menu.pack(fill="both", expand=True)
        menu.grid_rowconfigure(1, weight=1)
        menu.grid_columnconfigure(0, weight=1)

        dir_path=Path(__file__).parent/"Images"
        icon_path=dir_path/"icon.png"
        icon=PhotoImage(file=icon_path)
        root.iconphoto(False, icon)

        game1_path=dir_path/"tic-tac-toe.png"
        game1_icon=Image.open(game1_path)
        re_game1_icon=game1_icon.resize((100,100))
        img1=ImageTk.PhotoImage(re_game1_icon)

        game2_path=dir_path/"connect-four.jpg"
        game2_icon=Image.open(game2_path)
        re_game2_icon=game2_icon.resize((100,100))
        img2=ImageTk.PhotoImage(re_game2_icon)
        
        game3_path=dir_path/"minesweeper.png"
        game3_icon=Image.open(game3_path)
        re_game3_icon=game3_icon.resize((100,100))
        img3=ImageTk.PhotoImage(re_game3_icon)
        
        game4_path=dir_path/"wordle.webp"
        game4_icon=Image.open(game4_path)
        re_game4_icon=game4_icon.resize((100,100))
        img4=ImageTk.PhotoImage(re_game4_icon)

        game5_path=dir_path/"typing-test.png"
        game5_icon=Image.open(game5_path)
        re_game5_icon=game5_icon.resize((100,100))
        img5=ImageTk.PhotoImage(re_game5_icon)
        
        title_font=tkFont.Font(family="Impact", size=30)
        label_title=tk.Label(menu, text="Games.py", font=title_font)
        label_title.grid(row=0, column=0, pady=(40, 20))
        games_frame=tk.Frame(menu)
        games_frame.grid(row=1, column=0)
        
        def launch_tic_tac_toe():
                menu.forget()
                root.title("Tic Tac Toe")
                root.configure(bg="light yellow")
                game1_font=tkFont.Font(family="Impact", size=30)
                game1_title=tk.Label(root, text="Tic Tac Toe", font=game1_font)
                game1_title.pack(side="top", pady=5)
                game1_frame=tk.Frame(root, width=600, height=600, bg="lightgrey")
                game1_frame.pack(side="top", pady=5)
                game1_frame.pack_propagate(False)

                stop_game=game_1.run_game(game1_frame, root)

                def return_to_menu():
                        stop_game()
                        root.title("Games")
                        game1_frame.destroy()
                        game1_title.destroy()
                        return_button.destroy()
                        menu.pack(fill="both", expand=True)

                return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
                return_button.pack(side="top", pady=20)

        def launch_connect_4():
                menu.forget()
                root.title("Connect 4")
                root.configure(bg="light yellow")
                game2_font=tkFont.Font(family="Impact", size=30)
                game2_title=tk.Label(root, text="Connect 4", font=game2_font)
                game2_title.pack(side="top", pady=5)
                game2_frame=tk.Frame(root, width=700, height=600, bg="lightgrey")
                game2_frame.pack(side="top", pady=5)
                game2_frame.pack_propagate(False)
               
                stop_game=game_2.run_game(game2_frame, root)
               
                def return_to_menu():
                        stop_game()
                        root.title("Games")
                        game2_frame.destroy()
                        game2_title.destroy()
                        return_button.destroy()
                        menu.pack(fill="both", expand=True)
               
                return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
                return_button.pack(side="top", pady=20)

        def launch_minesweeper():
               menu.forget()
               root.title("Minesweeper")
               root.configure(bg="light yellow")
               game3_font=tkFont.Font(family="Impact", size=30)
               game3_title=tk.Label(root, text="Minesweeper", font=game3_font)
               game3_title.pack(side="top", pady=5)
               game3_frame=tk.Frame(root, width=600, height=600, bg="lightgrey")
               game3_frame.pack(side="top", pady=5)
               game3_frame.pack_propagate(False)

               stop_game=game_3.run_game(game3_frame, root)

               def return_to_menu():
                      stop_game()
                      root.title("Games")
                      game3_frame.destroy()
                      game3_title.destroy()
                      return_button.destroy()
                      menu.pack(fill="both", expand=True)

               return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
               return_button.pack(side="top", pady=20)

        def launch_wordle():
               menu.forget()
               root.title("Wordle")
               root.configure(bg="light yellow")
               game4_font=tkFont.Font(family="Impact", size=30)
               game4_title=tk.Label(root, text="Wordle", font=game4_font)
               game4_title.pack(side="top", pady=5)
               game4_frame=tk.Frame(root, width=600, height=600, bg="lightgrey")
               game4_frame.pack(side="top", pady=5)
               game4_frame.pack_propagate(False)

               stop_game=game_4.run_game(game4_frame, root)

               def return_to_menu():
                      stop_game()
                      root.title("Games")
                      game4_frame.destroy()
                      game4_title.destroy()
                      return_button.destroy()
                      menu.pack(fill="both", expand=True)

               return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
               return_button.pack(side="top", pady=20)

        def launch_type_practice():
               menu.forget()
               root.title("Type Practice")
               root.configure(bg="light yellow")
               game5_font=tkFont.Font(family="Impact", size=30)
               game5_title=tk.Label(root, text="Type Practice", font=game5_font)
               game5_title.pack(side="top", pady=5)
               game5_frame=tk.Frame(root, width=1200, height=600, bg="black")
               game5_frame.pack(side="top", pady=5)
               game5_frame.pack_propagate(False)

               stop_game=game_5.run_game(game5_frame, root)

               def return_to_menu():
                      stop_game()
                      root.title("Games")
                      game5_frame.destroy()
                      game5_title.destroy()
                      return_button.destroy()
                      menu.pack(fill="both", expand=True)

               return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
               return_button.pack(side="top", pady=20)

        button_1=tk.Button(games_frame, text="Tic Tac Toe", image=img1, command=launch_tic_tac_toe)
        button_1.pack(side="left", padx=5)

        button_2=tk.Button(games_frame, text="Connect 4", image=img2, command=launch_connect_4)
        button_2.pack(side="left", padx=5)

        button_3=tk.Button(games_frame, text="Minesweeper", image=img3, command=launch_minesweeper)
        button_3.pack(side="left", padx=5)

        button_4=tk.Button(games_frame, text="Wordle", image=img4, command=launch_wordle)
        button_4.pack(side="left", padx=5)

        button_5=tk.Button(games_frame, text="Type Practice", image=img5, command=launch_type_practice)
        button_5.pack(side="left", padx=5)

        exit=tk.Button(menu, text="Quit", width=50, command=root.destroy)
        exit.grid(row=2, column=0, pady=(10, 50))

        root.mainloop()
        
if __name__ == "__main__":
    main()