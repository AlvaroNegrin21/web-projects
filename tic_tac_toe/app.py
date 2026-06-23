"""
Tic-Tac-Toe (Web)
--------------------
A Flask + JavaScript tic-tac-toe game. The board state and game
rules live entirely on the server; the frontend only sends moves
and renders the JSON response.

Endpoints:
    GET  /            - serves the game page
    GET  /state        - returns the current board state
    POST /move          - plays a move at the given index
    POST /reset          - resets the game
"""

from flask import Flask, render_template, jsonify, request
import game

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/state")
def state():
    """Returns the current board, player, and winner."""
    return jsonify({
        "board": game.board,
        "current_player": game.current_player,
        "winner": game.winner,
        "winning_combo": game.winning_combo,
        "scores": game.scores
    })


@app.route("/move", methods=["POST"])
def move():
    """Receives a move (cell index) and applies it if legal."""
    data = request.get_json()
    index = data.get("index")

    success = game.make_move(index)

    return jsonify({
        "success": success,
        "board": game.board,
        "current_player": game.current_player,
        "winner": game.winner,
        "winning_combo": game.winning_combo,
        "scores": game.scores
    })


@app.route("/reset", methods=["POST"])
def reset():
    """Resets the game to a fresh board."""
    game.reset_game()
    return jsonify({
        "board": game.board,
        "current_player": game.current_player,
        "winner": game.winner,
        "winning_combo": game.winning_combo,
        "scores": game.scores
    })


if __name__ == "__main__":
    app.run(debug=True)