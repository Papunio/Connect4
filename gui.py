import tkinter as tk
from main import Game
from time import sleep


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

        self.game = Game(r, c)

        self.draw_rect_board()

        self.gui_board.bind('<Button-1>', self.clicked)

        self.root.mainloop()

    def draw_gui_board(self):
        self.gui_board.delete('oval')
        for i in range(self.r):
            for j in range(self.c):
                if self.game.board[i][j] == "X":  # Kolor zolty
                    self.draw_oval(i, j, '#f1c40f')
                elif self.game.board[i][j] == "O":  # Kolor czerwony
                    self.draw_oval(i, j, '#c93e34')

    def draw_rect_board(self):
        for i in range(self.r):
            for j in range(self.c):
                self.gui_board.create_rectangle((self.size + 2 * self.space) * j + self.space,
                                                (self.size + 2 * self.space) * i + self.space,
                                                self.size + (self.size + 2 * self.space) * j + self.space,
                                                self.size + (self.size + 2 * self.space) * i + self.space,
                                                fill='#4653db',
                                                outline='white')

    def draw_oval(self, i, j, c):
        self.gui_board.create_oval((self.size + 2 * self.space) * j + self.space + 1,
                                   (self.size + 2 * self.space) * i + self.space + 1,
                                   self.size + (self.size + 2 * self.space) * j + self.space - 1,
                                   self.size + (self.size + 2 * self.space) * i + self.space - 1,
                                   fill=c,
                                   outline=c)  # Czy jednak zostawic czarne

    def clicked(self, event):  # Klopoty z precyzja przy space > 0
        self.game.click(event.x // (self.size + self.space))
        self.draw_gui_board()
        if self.game.end:
            self.win_screen()

    def win_screen(self):  # Trzeba zrobić ładniej
        if self.game.player_turn == "O":  # Zrobic ladniejsze, czystszy kod
            self.w1 = tk.Label(self.root, text="Yellow player won!")
            self.w2 = tk.Label(self.root, text="Press space to play again")
        else:
            self.w1 = tk.Label(self.root, text="Red player won!")
            self.w2 = tk.Label(self.root, text="Click to play again")

        self.w1.pack()
        self.w2.pack()
        self.gui_board.unbind("<Button-1>")
        self.root.bind("<space>", self.reset_game)

    def reset_game(self, event):
        self.root.unbind("<space>")
        self.w1.destroy()
        self.w2.destroy()
        self.game.reset()
        self.gui_board.bind('<Button-1>', self.clicked)
        self.draw_rect_board()

    def empty(self, event):
        pass


if __name__ == "__main__":
    greet = StartWindow()
