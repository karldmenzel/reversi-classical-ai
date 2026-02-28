
from reversi import reversi
from greedy_player import choose_move as player_1_move
from greedy_bfs_player import choose_move as player_2_move

class AIGameServer:
    def __init__(self, player1, player2):
        """
        player1 = white (turn = 1)
        player2 = black (turn = -1)
        """
        self.game = reversi()
        self.player1 = player1
        self.player2 = player2
        self.turn = 1  # White starts

    def play_game(self):
        consecutive_passes = 0

        while True:
            current_player = self.player1 if self.turn == 1 else self.player2

            # Ask AI for move
            move = current_player(self.turn, self.game.board.copy(), self.game)

            x, y = move

            # Player passes
            if x == -1 and y == -1:
                consecutive_passes += 1
                print(f"Player {'White' if self.turn == 1 else 'Black'} passes.")
            else:
                result = self.game.step(x, y, self.turn)

                if result >= 0:
                    consecutive_passes = 0
                    print(f"Player {'White' if self.turn == 1 else 'Black'} plays ({x},{y})")
                else:
                    # Illegal move → treat as pass
                    consecutive_passes += 1
                    print(f"Illegal move by {'White' if self.turn == 1 else 'Black'} → treated as pass.")

            # End condition
            if consecutive_passes >= 2:
                break

            # Switch turn
            self.turn *= -1

        self.print_result()

    def print_result(self):
        white = self.game.white_count
        black = self.game.black_count

        print("\nFinal Board:")
        print(self.game.board)

        print(f"\nFinal Score:")
        print(f"White: {white}")
        print(f"Black: {black}")

        if white > black:
            print("White Wins!")
        elif black > white:
            print("Black Wins!")
        else:
            print("Draw!")

if __name__ == "__main__":
    server = AIGameServer(
        player1=player_2_move,  # White
        player2=player_1_move   # Black
    )

    server.play_game()