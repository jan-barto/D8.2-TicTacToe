class TicTacToeGame:
    def __init__(self):
        self.game_board = [
            ["   ", " a ", " b ", " c "],
            [" 1 ", " - ", " - ", " - "],
            [" 2 ", " - ", " - ", " - "],
            [" 3 ", " - ", " - ", " - "]
        ]
        self.player = "X"

    def print_board(self):
        for row in self.game_board:
            to_print = ""
            for letter in row:
                to_print += str(letter)
            print(to_print)

    def player_turn(self):
        who = self.player
        koo = input(f'Zadej koordinát (ve formátu: c1, b3, apod.), hraje hráč "---{who}---": ')
        # koo = "a2"
        x_list = ["a", "b", "c"]
        y_list = ["1", "2", "3"]
        try:
            x = x_list.index(koo[0])
            y = y_list.index(koo[1])
        except (KeyError, ValueError, IndexError):
            print("Chybné zadání. Opakuj zadání.")
            self.player_turn()
        else:
            to_fill = self.game_board[y + 1][x + 1]
            if to_fill == " X " or to_fill == " O ":
                print("Pole obsazeno. Opakuj zadání.")
                self.player_turn()
            else:
                self.game_board[y + 1][x + 1] = f" {who} "

    def change_player(self):
        if self.player == "X":
            self.player = "O"
        else:
            self.player = "X"

    def check_winner(self):
        board = self.game_board
        # rows
        for row in board:
            if (row[1] == row[2] == row[3] == " X ") or (row[1] == row[2] == row[3] == " O "):
                return f"Vítěz je Hráč {row[1]}! Blahopřeji!"
        # columns
        for col in range(1, 4):
            if (board[1][col] == board[2][col] == board[3][col] == " X ") or (
                    board[1][col] == board[2][col] == board[3][col] == " O "):
                return f"Vítěz je Hráč {board[1][col]}! Blahopřeji!"
        # diagonals
        if (board[1][1] == board[2][2] == board[3][3] == " X ") or (board[1][1] == board[2][2] == board[3][3] == " O "):
            return f"Vítěz je Hráč {board[1][1]}! Blahopřeji!"
        elif (board[3][1] == board[2][2] == board[1][3] == " X ") or (
                board[3][1] == board[2][2] == board[1][3] == " O "):
            return f"Vítěz je Hráč {board[3][1]}! Blahopřeji!"

        # empty field
        empty = False
        for row in board:
            for letter in row:
                if letter == " - ":
                    empty = True
        if not empty:
            return "Hrací pole je plné. Je to remíza."

    def the_play(self):
        self.print_board()
        self.player_turn()
        self.change_player()


ttt = TicTacToeGame()

game_on = True

while game_on:
    if ttt.check_winner():
        print(ttt.check_winner())
        game_on = False
        break
    ttt.the_play()
