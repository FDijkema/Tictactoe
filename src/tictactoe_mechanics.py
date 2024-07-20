import numpy as np


class TictactoeGame:
    def __init__(self):
        self.state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player_name = {
            1: "Player 1",
            -1: "Player 2"
        }
        self.next_to_move = 1    # 1 for player 1, -1 for player 2
        self.winner = None
        self.game_over = False

    def move(self, row, column):
        # convert to 0-base indexing
        row = row - 1
        column = column - 1
        if self.game_over:    # can't make a move after the game ended
            print("This game is already decided. You can't play anymore.")
        elif self.state[row, column] == 0:    # check if the field is empty
            self.state[row, column] = self.next_to_move    # update the game state
            if self.is_winning_move(row, column):
                self.winner = self.player_name[self.next_to_move]
                print("Congratulations! {} wins!".format(self.winner))
            self.next_to_move *= -1    # advance the game to the next move
        else:   # can't make a move on filled field
            print("This move is invalid. Try an empty field instead.")

    def is_winning_move(self, row, column):
        row_sum = abs(np.sum(self.state[row, :]))
        column_sum = np.abs(np.sum(self.state[:, column]))
        diag_sum_left = np.abs(np.sum(np.diag(self.state)))
        diag_sum_right = np.abs(np.sum(np.diag(np.fliplr(self.state.copy()))))
        winning_configurations = (
            row_sum == 3,
            column_sum == 3,
            diag_sum_left == 3,
            diag_sum_right == 3
        )
        # close_calls = (
        #    row_sum == 2,
        #    column_sum == 2,
        #    diag_sum_left == 2,
        #    diag_sum_right == 2)
        if any(winning_configurations):
            self.game_over = True
            return True
        # elif sum(close_calls) >= 2:    # win in the next round guaranteed
        #    self.game_over = True
        #    return True    # also signal that the game has been won already
        else:
            return False
