def calculate_final_score(board):
    black_tiles = 0
    white_tiles = 0
    for row in board:
        for tile in row:
            if tile == -1:
                black_tiles += 1
            elif tile == 1:
                white_tiles += 1
    print("white score", white_tiles, "black score", black_tiles)

    return white_tiles, black_tiles