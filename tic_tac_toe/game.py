"""
Tic-Tac-Toe game logic: board state, move validation, and
win/draw detection.
"""

board = [""] * 9
current_player = "X"
winner = None
winning_combo = None
scores = {"X": 0, "O": 0, "Draw": 0}

def reset_game():
    """Resets the board to a fresh empty game."""
    global board, current_player, winner, winning_combo
    board = [""] * 9
    current_player = "X"
    winner = None
    winning_combo = None


def make_move(index):
    """Places the current player's symbol at the given index, if legal.

    Args:
        index (int): board position (0-8) to play.

    Returns:
        bool: True if the move was made, False if it was illegal
        (cell occupied, game already over, or invalid index).
    """
    global current_player, winner, winning_combo

    if winner is not None:
        return False
    if index < 0 or index > 8:
        return False
    if board[index] != "":
        return False

    board[index] = current_player
    winner, winning_combo = check_winner()

    if winner is not None:
        scores[winner] += 1
    else:
        current_player = "O" if current_player == "X" else "X"
        
    return True


def check_winner():
    """Checks the board for a winner or a draw.

    Returns:
        tuple: (winner, winning_combo) where winner is "X", "O", "Draw",
        or None, and winning_combo is the list of 3 indices that won,
        or None if there's no winner yet.
    """
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6],             # diagonals
    ]

    for combo in win_combinations:
        a, b, c = combo
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a], combo

    if "" not in board:
        return "Draw", None

    return None, None