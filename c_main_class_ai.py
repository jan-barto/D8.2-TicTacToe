import random


class TicTacToeGame:
    def __init__(self):
        self.game_board = [
            ["   ", " a ", " b ", " c "],
            [" 1 ", " - ", " - ", " - "],
            [" 2 ", " - ", " - ", " - "],
            [" 3 ", " - ", " - ", " - "]
        ]
        self.player = "X"
        self.x_list = ["a", "b", "c"]
        self.y_list = ["1", "2", "3"]

    def print_board(self):
        for row in self.game_board:
            to_print = ""
            for letter in row:
                to_print += str(letter)
            print(to_print)

    def player_turn(self):
        koo = input(f'Hraje hráč. Zadej koordinát (ve formátu: c1, b3, apod.): ')
        try:
            x = self.x_list.index(koo[0])
            y = self.y_list.index(koo[1])
        except (KeyError, ValueError, IndexError):
            print("Chybné zadání. Opakuj zadání.")
            self.player_turn()
        else:
            to_fill = self.game_board[y + 1][x + 1]
            if to_fill == " X " or to_fill == " O ":
                print("Pole obsazeno. Opakuj zadání.")
                self.player_turn()
            else:
                self.game_board[y + 1][x + 1] = " X "

    def comp_turn(self):
        print("Hraje počítač.")
        try:
            x = self.x_list.index(random.choice(self.x_list))
            y = self.y_list.index(random.choice(self.y_list))
        except (KeyError, ValueError, IndexError):
            print("Chybné zadání. Opakuj zadání.")
            self.comp_turn()
        else:
            to_fill = self.game_board[y + 1][x + 1]
            if to_fill == " X " or to_fill == " O ":
                self.comp_turn()
            else:
                self.game_board[y + 1][x + 1] = " O "

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

    def print_result(self):
        self.print_board()
        print(self.check_winner())

    def the_play(self):
        while True:
            self.print_board()
            self.player_turn()
            if self.check_winner():
                self.print_result()
                return False
            self.comp_turn()
            if self.check_winner():
                self.print_result()
                return False


ttt = TicTacToeGame()
ttt.the_play()
