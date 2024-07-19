import numpy as np


class TictactoeGame:
    def __init__(self):
        self.state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player_name = ["Player 1", "Player 2"]
        self.next_to_move = 1    # 1 for player 1, -1 for player 2
        self.winner = None
        self.game_over = False

    def move(self, row, column):
        if self.game_over:    # can't make a move after the game ended
            print("This game is already decided. You can't play anymore.")
        elif self.state[row, column] == 0:    # check if the field is empty
            self.state[row, column] = self.next_to_move    # update the gamestate
            if self.is_winning_move(row, column):
                self.winner = self.player_name[self.next_to_move]
                print("Congratulations! {} wins!".format(self.winner))
            self.next_to_move *= -1    # advance the game to the next move
        else:   # can't make a move on filled field
            print("This move is invalid.")

    def is_winning_move(self, row, column):
        # winning on row todo
        # winning on column todo
        # winning on diagonal todo
        # winning by no more moves to make todo
        self.game_over = True
        return True


