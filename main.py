class Game:
    def __init__(self, r=6, c=7, w=4):
        self.columns = c
        self.rows = r
        self.to_win = w
        self.players = [1, 2]
        self.move_count = 0
        self.player_turn = 1
        self.board = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.legal = [self.rows - 1 for _ in range(self.columns)]
        self.end = False
        self.tie = False

    def click(self, move):
        if self.legal[move] == -1:
            print("This column is full, try again")
            return
        self.board[self.legal[move]][move] = self.player_turn
        self.check_win(move)
        self.legal[move] -= 1
        self.player_turn = 1 if self.player_turn == 2 else 2
        self.move_count += 1
        if self.move_count >= self.columns * self.rows and not self.end:
            self.tie = True

    def check_win(self, c):
        self.check_column(c)
        self.check_row(c)
        self.check_diag(c)

    def check_column(self, c):
        if self.legal[c] + self.to_win <= self.rows:
            in_column = 1
            cur_row = self.legal[c] + 1
            while cur_row < self.rows and self.board[cur_row][c] == self.player_turn:
                in_column += 1
                cur_row += 1
            if in_column >= self.to_win:
                self.end = True

    def check_row(self, c):
        i, j, in_row = c - 1, c + 1, 1
        while i >= 0 and self.board[self.legal[c]][i] == self.player_turn:
            in_row += 1
            i -= 1

        while j < self.rows and self.board[self.legal[c]][j] == self.player_turn:
            in_row += 1
            j += 1
        if in_row >= self.to_win:
            self.end = True

    def check_diag(self, c):
        k, w, score = c - 1, self.legal[c] - 1, 1
        while k >= 0 and w >= 0 and self.board[w][k] == self.player_turn:
            score += 1
            k -= 1
            w -= 1

        k, w = c + 1, self.legal[c] + 1
        while k < self.columns and w < self.rows and self.board[w][k] == self.player_turn:
            score += 1
            k += 1
            w += 1
        if score >= self.to_win:
            self.end = True

        k, w, score = c - 1, self.legal[c] + 1, 1
        while k >= 0 and w < self.rows and self.board[w][k] == self.player_turn:
            score += 1
            k -= 1
            w += 1

        k, w = c + 1, self.legal[c] - 1
        while k < self.columns and w >= 0 and self.board[w][k] == self.player_turn:
            score += 1
            k += 1
            w -= 1
        if score >= self.to_win:
            self.end = True

    def reset(self):
        self.move_count = 0
        self.player_turn = 1
        self.board = [[0 for j in range(self.columns)] for i in range(self.rows)]
        self.legal = [self.rows - 1 for _ in range(self.columns)]
        self.end = False
        self.tie = False


if __name__ == "__main__":
    run = Game()
