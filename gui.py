import tkinter as tk
from main import Game


class StartWindow:  # Można jakoś ładniej zrobić.... (canvas? / grid?)
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect4")
        self.window.geometry("220x170")
        self.window.resizable(False, False)
        ask_cols = tk.Label(text="How many columns?")
        ask_rows = tk.Label(text="How many rows?")
        self.cols_slider = tk.Scale(
            self.window,
            from_=4,
            to=10,
            orient='horizontal',
        )
        self.rows_slider = tk.Scale(
            self.window,
            from_=4,
            to=10,
            orient='horizontal',
        )
        self.cols_slider.set(7)
        self.rows_slider.set(6)
        play_button = tk.Button(self.window, text="PLAY", command=self.open_game)
        ask_cols.pack()
        self.cols_slider.pack()
        ask_rows.pack()
        self.rows_slider.pack()
        play_button.pack()
        self.window.mainloop()

    def open_game(self):  # Tutaj po prostu odpalamy okno glowne programu
        self.window.withdraw()  # Ukrycie
        main_window = GameWindow(self.rows_slider.get(), self.cols_slider.get())
        # game = Game(self.rows_slider.get(), self.cols_slider.get())
        # self.window.destroy()


class GameWindow:  # Okno główne programu
    def __init__(self, r, c):
        self.size = 80
        self.space = 0
        self.root = tk.Tk()
        self.r = r
        self.c = c
        self.res_x = r * self.size + r * 2 * self.space
        self.res_y = c * self.size + c * 2 * self.space
        self.root.title("Connect4")
        self.root.geometry(f"{self.res_y}x{self.res_x}")
        self.root.resizable(False, False)

        self.gui_board = tk.Canvas(self.root, width=self.res_y, height=self.res_x)
        self.gui_board.place(x=0, y=0)

        self.game = Game()

        self.draw_gui_board()

        self.root.mainloop()

    def draw_gui_board(self):
        self.gui_board.delete('all')
        for i in range(self.r):
            for j in range(self.c):
                if self.game.board[i][j] == "X":
                    self.gui_board.create_rectangle((self.size + 2 * self.space) * j + self.space,
                                                    (self.size + 2 * self.space) * i + self.space,
                                                    self.size + (self.size + 2 * self.space) * j + self.space,
                                                    self.size + (self.size + 2 * self.space) * i + self.space,
                                                    fill='#c93e34',
                                                    tags=f'{i},{j}')
                    self.gui_board.tag_bind(f'{i},{j}', '<Button-1>', self.clicked)
                elif self.game.board[i][j] == "O":
                    self.gui_board.create_rectangle((self.size + 2 * self.space) * j + self.space,
                                                    (self.size + 2 * self.space) * i + self.space,
                                                    self.size + (self.size + 2 * self.space) * j + self.space,
                                                    self.size + (self.size + 2 * self.space) * i + self.space,
                                                    fill='#4653db',
                                                    tags=f'{i},{j}')
                    self.gui_board.tag_bind(f'{i},{j}', '<Button-1>', self.clicked)
                else:
                    self.gui_board.create_rectangle((self.size + 2 * self.space) * j + self.space,
                                                    (self.size + 2 * self.space) * i + self.space,
                                                    self.size + (self.size + 2 * self.space) * j + self.space,
                                                    self.size + (self.size + 2 * self.space) * i + self.space,
                                                    fill='#f1c40f',
                                                    tags=f'{i},{j}')
                    self.gui_board.tag_bind(f'{i},{j}', '<Button-1>', self.clicked)

    def clicked(self, event):  # Klopoty z precyzja przy space > 0
        self.game.click(event.x // self.size)
        self.draw_gui_board()
        if self.game.end:
            self.win_screen()

    def win_screen(self):  # Można zrobić ładniej
        self.root.withdraw()
        self.win = tk.Tk()
        self.win.title("Connect4")
        self.win.geometry("200x50")
        self.win.resizable(False, False)
        if self.game.player_turn == "O":
            winner = tk.Label(self.win, text="Red player won!")
        else:
            winner = tk.Label(self.win, text="Blue player won!")

        reset_button = tk.Button(self.win, text="Rematch", command=self.reset_game)

        winner.pack()
        reset_button.pack()
        self.win.mainloop()

    def reset_game(self):
        self.game.reset()
        self.root.deiconify()
        self.draw_gui_board()
        self.win.destroy()


if __name__ == "__main__":
    greet = StartWindow()
