"""This module takes care of the game mechanics of tictactoe, so you can focus on the UI"""

import numpy as np


class TictactoeGame:
    """
        A class performing the mechanics of a game of Tictactoe.

        ...

        Attributes
        ----------
        state : numpy.ndarray
            keeps track of the state of the game board
            filled with 0 at the beginning of the game
            1 represents a move by player 1
            -1 represents a move by player 2
        self.player_name : dict
            links the name of the player (player 1 or player 2) to the symbol (1 or -1)
        next_to_move : int
            what symbol is used by the player who will make the next move
            can be 1 or -1
        winner : str
            who wins the game?
            returns None while the game is undecided
            Possible values after Game over: "Player 1", "Player 2" or "Draw"
        game_over : bool
            whether the game is decided or not
        number_of_moves : int
            number of moves made in the game so far

        Methods
        -------
        __init__():
            initializes the game board
        move(row: int, column: int):
            advances the game by placing the symbol of the player who is next to move on the board
            at the indicated row and column
            row and column index starts from 0
            updates class attributes accordingly if the game has ended in win or draw
        """
    def __init__(self):
        """initiates a new game board"""
        self.state = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player_name = {
            1: "Player 1",
            -1: "Player 2"
        }
        self.next_to_move = 1    # 1 for player 1, -1 for player 2
        self.winner = None
        self.game_over = False
        self.number_of_moves = 0

    def move(self, row, column):
        """
        advances the game by placing the symbol of the player who is next to move on the board

        Parameters
        ----------
        row: int
            row index where the player will move (base 0)
        column: int
            column index where the player will move (base 0)
        """
        if not (row in [0, 1, 2] and column in [0, 1, 2]):    # make sure the move fits on the board
            raise IndexError("Your move does not fit on the Tictactoe board."
                             "Make sure row and column indices are between 1 and 3.")
        if self.game_over:    # can't make a move after the game ended
            raise Exception("This game is already decided. You can't play anymore.")
        elif self.state[row, column] == 0:    # check if the field is empty
            self.state[row, column] = self.next_to_move    # place player symbol in the right field
            self.number_of_moves += 1
            # evaluate the result of the move
            if self._is_winning_move(row, column):    # game ends by win
                self.game_over = True
                self.winner = self.player_name[self.next_to_move]
                print("Congratulations! {} wins!".format(self.winner))
            elif self.number_of_moves == 9:   # game ends by draw
                self.game_over = True
                self.winner = "Draw"
                print("No more moves to make. The game ends in a draw.")
            else:    # just a normal move in the game
                pass
            self.next_to_move *= -1    # advance the game to the next move
        else:   # can't make a move on filled field
            raise ValueError("You have already made move on this field. Try an empty field instead.")

    def _is_winning_move(self, row, column):
        """returns a boolean value indicating whether the game has ended in a win
            the check is made based on the game_state, row and column are only passed to check
            the board more efficiently"""
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
            return True
        # elif sum(close_calls) >= 2:    # win in the next round guaranteed
        #    return True    # also signal that the game has been won already
        else:
            return False
