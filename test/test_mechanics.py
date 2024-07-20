import numpy as np
from src.tictactoe_mechanics import TictactoeGame


def test_game_initialization():
    my_game = TictactoeGame()
    assert np.array_equal(my_game.state, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    assert my_game.game_over is False


def test_game_simple_player_1_wins():
    my_game = TictactoeGame()
    my_game.move(1,1)    # player 01
    my_game.move(2,1)    # player 02
    my_game.move(1,2)    # player 01
    my_game.move(3,2)    # player 02
    my_game.move(1,3)    # player 01 wins
    assert np.array_equal(my_game.state, np.array([[1, 1, 1], [-1, 0, 0], [0, -1, 0]]))
    assert my_game.game_over
    assert my_game.winner == "Player 1"


# def test_game_player_1_wins_before_final_move():
#     my_game = TictactoeGame()
#     my_game.move(1, 1)    # player 01
#     my_game.move(2, 1)    # player 02
#     my_game.move(1, 3)    # player 01
#     my_game.move(1, 2)    # player 02
#     my_game.move(3, 3)    # player 01 wins
#     assert np.array_equal(my_game.state, np.array([[1, -1, 1], [-1, 0, 0], [0, 0, 1]]))
#     assert my_game.game_over
#     assert my_game.winner == "Player 1"


def test_game_player_2_wins():
    my_game = TictactoeGame()
    my_game.move(1, 2)    # player 01
    my_game.move(1, 1)    # player 02
    my_game.move(1, 3)    # player 01
    my_game.move(2, 2)    # player 02
    my_game.move(2, 3)    # player 01
    my_game.move(3, 3)    # player 02 wins
    assert np.array_equal(my_game.state, np.array([[-1, 1, 1], [0, -1, 1], [0, 0, -1]]))
    assert my_game.game_over
    assert my_game.winner == "Player 2"

def test_invalid_move():
    my_game = TictactoeGame()
    my_game.move(1, 2)  # player 01
    my_game.move(1, 2)  # player 02
    assert np.array_equal(my_game.state, np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]))
    assert my_game.next_to_move == -1
