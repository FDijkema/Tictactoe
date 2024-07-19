import numpy as np


class Tictactoe_game():
    def __init__(self):
        self.game_state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player_name = ["Player 1", "Player 2"]
        self.next_to_move = 1    # 1 for player 1, -1 for player 2
        self.winner = None
        self.game_over = False

    def make_move(self, row, column):
        if self.game_over:    # can't make a move after the game ended
            print("This game is already decided. You can't play anymore.")
        else:   # the game is still undecided, make the move
            self.game_state[row, column] = self.next_to_move    # update the gamestate
            if self.is_winning_move(row, column):
                self.winner = self.player_name[self.next_to_move]
                print("Congratulations! {} wins!".format(self.winner))
            self.next_to_move *= -1    # advance the game to the next move

    def is_winning_move(self, row, column):
        return True


