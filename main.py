class Game:
    def __init__(self, r=6, c=7, w=4):
        self.columns = c
        self.rows = r
        self.to_win = w
        self.players = ['O', 'X']
        self.p = 0
        self.move_count = 0
        self.player_turn = 'X'
        self.board = [[' ' for j in range(self.columns)] for i in range(self.rows)]
        self.legal = [self.rows - 1 for _ in range(self.columns)]
        self.end = False
        self.game_loop()

    def game_loop(self):
        while not self.end and self.move_count <= self.columns * self.rows:
            self.draw_board()
            move = int(input(f"Player{self.p + 1} Column> "))
            if move > self.columns or move < 0:
                print("Wrong column number, try again")
                continue
            if self.legal[move] == -1:
                print("This column is full, try again")
                continue
            self.board[self.legal[move]][move] = self.player_turn
            self.check_win(move)
            self.legal[move] -= 1
            self.player_turn = self.players[self.p]
            self.p = (self.p + 1) % len(self.players)
            self.move_count += 1
        self.draw_board()
        self.win_screen()

    def check_win(self, c):  # Jeszcze ukosy..
        self.check_column(c)
        self.check_row(c)
        self.check_diag(c)

    def check_column(self, c):
        if self.legal[c] + self.to_win <= self.rows:
            in_row = 1
            cur_row = self.legal[c] + 1
            while cur_row < self.rows:
                if self.board[cur_row][c] == self.player_turn:
                    in_row += 1
                cur_row += 1
            if in_row >= self.to_win:
                self.end = True

    def check_row(self, c):
        i, j, in_row = c - 1, c + 1, 1
        while i >= 0:
            if self.board[self.legal[c]][i] == self.player_turn:
                in_row += 1
                i -= 1
            else:
                break
        while j < self.rows:
            if self.board[self.legal[c]][j] == self.player_turn:
                in_row += 1
                j += 1
            else:
                break
        if in_row >= self.to_win:
            self.end = True
            return

    def check_diag(self, c):  # Nalezy sprawdzic obie przekatne, self.legal(c) -> wiersz w ktorym jest postawiony zeton
        k, w, score = c, self.legal[
            c], 1  # Wystarczy robić iteracje po przekatnej (podobnie jak przy poziomie), pilnowac zakresu
        # print(k, w)
        while k >= 0 and w >= 0:
            if self.board[w][k] == self.player_turn:
                score += 1
            k -= 1
            w -= 1
        k, w = c, self.legal[c]
        if score >= self.to_win:
            self.end = True

    def draw_board(self):
        for i in self.board:
            print(i)
        print('----' * self.columns)
        print('  ', end='')
        for j in range(self.columns):
            print(f'{j}, ', end='  ')
        print()

    def win_screen(self):
        print("-------------------------")
        print(f"Player {self.p} has won!")
        print("Click enter to play again")
        print("-------------------------")
        input()
        self.reset()

    def reset(self):
        self.p = 0
        self.move_count = 0
        self.player_turn = 'X'
        self.board = [[' ' for j in range(self.columns)] for i in range(self.rows)]
        self.legal = [self.rows - 1 for _ in range(self.columns)]
        self.end = False
        self.game_loop()


if __name__ == "__main__":
    run = Game()
