import numpy as np

class Game:

    def __init__(self):
        # Data
        self.game_on = True
        self.winner = 0
        self.players = [1, 2]
        self.change_player = 0
        # Start game matrix
        self.game_matrix = np.array([[0, 0, 0],
                                     [0, 0, 0],
                                     [0, 0, 0]])


    def check_rows_columns_cross(self, array):
        """
        Check if win_check = 1 - win player #1, if win_check = 2 - win player #2
        :param array:
        :return: win_check
        """
        win_check = 0
        if sum(array) == 3:
            win_check = 1
            return win_check
        elif sum(array) == 15:
            win_check = 2
            return win_check
        else:
            return win_check


    def check_left_right_cross_line(self):
        """
        Create left right cross line
        :return: left_right array numpy with this values
        """
        left_right = np.array([])
        for data in range(3):
            left_right = np.append(arr=left_right, values=self.game_matrix[data, data])

        return left_right


    def check_right_left_cross_line(self):
        """
        Create right left cross line
        :return: right_left array numpy with this values
        """
        right_left = np.array([])
        for data in range(3):
            right_left = np.append(arr=right_left, values=self.game_matrix[data, 2 - data])

        return right_left


    def check_winner(self, *args):
        # Check rows and columns
        for data in range(3):
            # Rows
            row_check = self.check_rows_columns_cross(self.game_matrix[data, :])
            if row_check > 0:
                self.winner = args[0]
                break

            # Columns
            column_check = self.check_rows_columns_cross(self.game_matrix[:, data])
            if column_check > 0:
                self.winner = args[0]
                break

            # Cross Left to Right
            check_left_right = self.check_rows_columns_cross(self.check_left_right_cross_line())
            if check_left_right > 0:
                self.winner = args[0]
                break

            # Cross Right to Left
            check_right_left = self.check_rows_columns_cross(self.check_right_left_cross_line())
            if check_right_left > 0:
                self.winner = args[0]
                break

        if self.winner > 0:
                self.game_on = False

        self.print_matrix()


    def is_full(self, game_matrix):
        """
        Check if all cells already used
        :param game_matrix:
        :return: True or False
        """
        result = all([True if cell > 0 else False for row in game_matrix for cell in row])
        return result


    def cell_already_used(self, player_x, player_y):
        """
        Check if current cells already used
        :param player_x:
        :param player_y:
        :return: True or False
        """
        if self.game_matrix[player_x, player_y] != 0:
            return True


    def print_matrix(self):
        """
        Print matrix in x/o style
        :return: print
        """
        list_matrix = np.array(self.game_matrix).tolist() # Convert into list

        # Convert all values into str
        for row in range(3):
            for cell in range(3):
                list_matrix[row][cell] = str(list_matrix[row][cell])
                # Change numbers to X/O symbols
                if list_matrix[row][cell] == "1":
                    list_matrix[row][cell] = "X"
                elif list_matrix[row][cell] == "5":
                    list_matrix[row][cell] = "O"
                else:
                    list_matrix[row][cell] = " "

        # Print with separators
        print("    c0   c1   c2")
        print("   "+"-" * 15)
        for row in list_matrix:
            print(f'r{list_matrix.index(row)}  '+"  |  ".join(row))
            print("   "+"-" * 15)


    def run_game(self):
        self.print_matrix()
        # Game
        while self.game_on:
            player = self.players[
                self.change_player % 2]  # Every time change player by modulus, index 0 or 1 in players list
            if not self.game_on: # Check game status
                break
            try:
                print(f"Player #{player} - chose your cell in format X and Y between 0-2")
                # User choices
                player_x = int(input("X:\n"))
                player_y = int(input("Y:\n"))
                if self.cell_already_used(player_x, player_y):
                    print(f"The cell {player_x}:{player_y} already used")
                    self.print_matrix()
                    continue
                if player == 1:
                    self.game_matrix[player_x, player_y] = 1
                else:
                    self.game_matrix[player_x, player_y] = 5
                self.check_winner(player)
                if not self.game_on:
                    self.print_matrix()
                    print(f"Game over. Player #{self.winner} WIN!")
                    break
            except (ValueError, IndexError):
                print("Invalid input! Enter two numbers from 0 to 2.")
                continue
            if self.is_full(self.game_matrix):
                print("Draw! Board is full!")
                break

            self.change_player += 1 # Change to next player


# Run
if __name__ == '__main__':
    game = Game()
    game.run_game()