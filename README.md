# Reversi Classical AI

The program is an AI built to play the game Reversi, without using machine learning techniques.

## How to Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip3 install -f requirements.txt`

## How To Run

1. Start the server. WARNING: Do not click the screen yet. `python3 src/reversi_server.py` (or Windows `python .\src\reversi_server.py`)
2. Start the professor's player. `python3 src/greedy_player.py` (or Windows `python .\src\greedy_player.py`)
3. Start our player. (Currently: greedy_bfs_player.py) `python3 src/greedy_bfs_player.py` (or Windows `python .\src\greedy_bfs_player.py`)
4. Click inside the game screen to start the game.
5. Click inside the game after it has ended to close the window.

Note: You may experience crashes/infinite loops if you try to close the screen before the game has ended.