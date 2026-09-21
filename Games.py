import tkinter as tk
from tkinter import PhotoImage
import tkinter.font as tkFont
import tic_tac_toe as game_1
import connect_4 as game_2
import minesweeper as game_3
from pathlib import Path
import os

def main():
        root=tk.Tk()
        root.geometry("2000x2500")
        root.title("Games")
        menu=tk.Frame(root)
        menu.pack(fill="both")

        title_font=tkFont.Font(family="Times", size=30)
        label_title=tk.Label(menu, text="Games.py", font=title_font)
        label_title.pack(side="top", pady=50)
        
        def launch_tic_tac_toe():
                menu.forget()
                root.title("Tic Tac Toe")
                game1_font=tkFont.Font(family="Times", size=30)
                game1_title=tk.Label(root, text="Tic Tac Toe", font=game1_font)
                game1_title.pack(side="top", pady=5)
                game1_frame=tk.Frame(root, width=600, height=600, bg="black")
                game1_frame.pack(side="top", pady=5)
                game1_frame.pack_propagate(False)

                stop_game=game_1.run_game(game1_frame, root)

                def return_to_menu():
                        stop_game()
                        root.title("Games")
                        game1_frame.destroy()
                        game1_title.destroy()
                        return_button.destroy()
                        menu.pack(fill="both")

                return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
                return_button.pack(side="top", pady=20)

        def launch_connect_4():
                menu.forget()
                root.title("Connect 4")
                game2_font=tkFont.Font(family="Times", size=30)
                game2_title=tk.Label(root, text="Connect 4", font=game2_font)
                game2_title.pack(side="top", pady=5)
                game2_frame=tk.Frame(root, width=700, height=600, bg="black")
                game2_frame.pack(side="top", pady=5)
                game2_frame.pack_propagate(False)
               
                stop_game=game_2.run_game(game2_frame, root)
               
                def return_to_menu():
                        stop_game()
                        root.title("Games")
                        game2_frame.destroy()
                        game2_title.destroy()
                        return_button.destroy()
                        menu.pack(fill="both")
               
                return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
                return_button.pack(side="top", pady=20)

        def launch_minesweeper():
               menu.forget()
               root.title("Minesweeper")
               game3_font=tkFont.Font(family="Times", size=30)
               game3_title=tk.Label(root, text="Minesweeper", font=game3_font)
               game3_title.pack(side="top", pady=5)
               game3_frame=tk.Frame(root, width=600, height=600, bg="black")
               game3_frame.pack(side="top", pady=5)
               game3_frame.pack_propagate(False)

               stop_game=game_3.run_game(game3_frame, root)

               def return_to_menu():
                      stop_game()
                      root.title("Games")
                      game3_frame.destroy()
                      game3_title.destroy()
                      return_button.destroy()
                      menu.pack(fill="both")

               return_button=tk.Button(root, text="Return to Menu", width=25, command=return_to_menu)
               return_button.pack(side="top", pady=20)
              
               

        button_1=tk.Button(menu, text="Tic Tac Toe", width=50, command=launch_tic_tac_toe)
        button_1.pack(side="top", pady=5)

        button_2=tk.Button(menu, text="Connect 4", width=50, command=launch_connect_4)
        button_2.pack(side="top", pady=5)

        button_3=tk.Button(menu, text="Minesweeper", width=50, command=launch_minesweeper)
        button_3.pack(side="top", pady=5)

        exit=tk.Button(menu, text="Quit", width=50, command=root.destroy)
        exit.pack(side="top", pady=50)

        root.mainloop()
        
if __name__ == "__main__":
    main()