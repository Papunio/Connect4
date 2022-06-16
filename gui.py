import tkinter as tk
from main import Game


class StartWindow:  # Można jakoś ładniej zrobić.... (canvas? / grid?) Chyba wypadałoby napisać od nowa..
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
        play_button = tk.Button(self.window, text="Play", command=self.open_game)
        ask_cols.pack()
        self.cols_slider.pack()
        ask_rows.pack()
        self.rows_slider.pack()
        play_button.pack()
        self.window.mainloop()

    def open_game(self):  # Tutaj po prostu odpalamy okno glowne programu
        # self.window.withdraw()
        GameWindow(self.rows_slider.get(), self.cols_slider.get())


class GameWindow:  # Okno główne programu

    def __init__(self, r, c):
        self.size = 80
        self.root = tk.Tk()
        self.r = r
        self.c = c
        self.res_x = r * self.size
        self.res_y = c * self.size
        self.root.title("Yellow player turn")
        self.root.geometry(f"{self.res_y}x{self.res_x}")
        self.root.resizable(False, False)

        self.gui_board = tk.Canvas(self.root, width=self.res_y, height=self.res_x)
        self.gui_board.place(x=0, y=0)

        self.game = Game(r, c)

        self.draw_rect_board()

        self.w1 = tk.Label(self.root, text="")
        self.tie = tk.Label(self.root, text="")
        self.rsmsg = tk.Label(self.root, text="")

        self.gui_board.bind('<Button-1>', self.clicked)

        self.root.mainloop()

    def draw_gui_board(self):
        self.gui_board.delete('oval')
        for i in range(self.r):
            for j in range(self.c):
                if self.game.board[i][j] == 1:  # Kolor zolty
                    self.draw_oval(i, j, '#f1c40f')
                elif self.game.board[i][j] == 2:  # Kolor czerwony
                    self.draw_oval(i, j, '#c93e34')

    def draw_rect_board(self):
        for i in range(self.r):
            for j in range(self.c):
                self.gui_board.create_rectangle(self.size * j, self.size * i,
                                                self.size + self.size * j,
                                                self.size + self.size * i,
                                                fill='#4653db',
                                                outline='#4653db')
                self.draw_oval(i, j, 'white')

    def draw_oval(self, i, j, c, off=2):
        self.gui_board.create_oval(self.size * j + off,
                                   self.size * i + off,
                                   self.size + self.size * j - off,
                                   self.size + self.size * i - off,
                                   fill=c,
                                   outline=c)  # Czy jednak zostawic czarne

    def clicked(self, event):
        self.game.click(event.x // self.size)
        self.draw_gui_board()
        if self.game.end:
            self.win_tie_screen(True)
        elif self.game.tie:
            self.win_tie_screen(False)

        self.root.title('Yellow player turn' if self.game.player_turn == 1 else 'Red player turn')

    def win_tie_screen(self, w):
        if w:
            self.w1 = tk.Label(self.root,
                               text='Red player won' if self.game.player_turn == 1 else 'Yellow player won')
            self.w1.pack()

        else:
            self.tie = tk.Label(self.root, text="Its a tie!")
            self.tie.pack()

        self.rsmsg = tk.Label(self.root, text="Press space to play again")
        self.rsmsg.pack()
        self.gui_board.unbind("<Button-1>")
        self.root.bind("<space>", self.reset_game)

    def reset_game(self, event):
        self.root.unbind("<space>")
        self.w1.destroy()
        self.tie.destroy()
        self.rsmsg.destroy()
        self.game.reset()
        self.gui_board.bind('<Button-1>', self.clicked)
        self.root.title("Yellow player turn")  # Zmienna
        self.draw_rect_board()

    def empty(self, event):
        pass


if __name__ == "__main__":
    greet = StartWindow()
