const cells = document.querySelectorAll('.cell');
const status = document.getElementById('status');
const resetButton = document.getElementById('reset');

let gameOver = false;

// Renders the board, status text, score, and winning highlight
// based on the latest game state received from the server.
function render(data) {
    gameOver = data.winner !== null;

    data.board.forEach((value, i) => {
        cells[i].textContent = value;
        cells[i].classList.remove('winner', 'x', 'o');

        if (value === "X") {
            cells[i].classList.add('x');
        } else if (value === "O") {
            cells[i].classList.add('o');
        }
    });

    // Highlight the winning combination, if any
    if (data.winning_combo) {
        data.winning_combo.forEach(i => {
            cells[i].classList.add('winner');
        });
    }

    if (data.winner) {
        status.textContent = data.winner === "Draw" ? "It's a draw!" : `Winner: ${data.winner}`;
    } else {
        status.textContent = `Turn: ${data.current_player}`;
    }

    document.getElementById('score-x').textContent = data.scores.X;
    document.getElementById('score-o').textContent = data.scores.O;
    document.getElementById('score-draw').textContent = data.scores.Draw;
}

// Sends a move to the server and re-renders the board with the response
function playMove(index) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ index: index })
    })
    .then(response => response.json())
    .then(data => render(data));
}

// Play a move when clicking a cell, unless the game has ended
cells.forEach(cell => {
    cell.addEventListener('click', () => {
        const index = parseInt(cell.dataset.index);
        if (!gameOver) {
            playMove(index);
        }
    });
});

// Reset the board (scores are preserved on the server)
resetButton.addEventListener('click', () => {
    fetch('/reset', { method: 'POST' })
        .then(response => response.json())
        .then(data => render(data));
});