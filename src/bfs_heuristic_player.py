#Zijie Zhang, Sep.24/2023

import numpy as np
import socket, pickle
from reversi import reversi
import time
from utils import calculate_final_score

def main():
    game_socket = socket.socket()
    game_socket.connect(('127.0.0.1', 33333))
    game = reversi()

    while True:

        #Receive play request from the server
        #turn : 1 --> you are playing as white | -1 --> you are playing as black
        #board : 8*8 numpy array
        data = game_socket.recv(4096)
        turn, board = pickle.loads(data)

        #Turn = 0 indicates game ended
        if turn == 0:
            calculate_final_score(board)
            game_socket.close()
            return
        
        #Debug info
        print(turn)
        print(board)
        calculate_final_score(board)

        #Local Greedy - Replace with your algorithm
        x = -1
        y = -1
        max = 0
        game.board = board
        best_move_list = []

        for i in range(8):
            for j in range(8):
                cur = game.step(i, j, turn, False)
                # any move that leads to a flipped piece is stored in the list
                if cur > 0:
                    # add tuple to move list where: cur=#of flipped tiles, i=x, j=y
                    best_move_list.append((cur, i, j))

        # no moves were found
        if len(best_move_list) == 0:
            x, y = (-1, -1)
        else:
            # sort the list in order of most flipped pieces, then choose the first best one
            print("best move list before:", best_move_list)
            mini_max(best_move_list, turn)
            print("best move list after minimax", best_move_list)
            best_move_list = sorted(best_move_list, key=lambda tup: tup[0], reverse=True)
            _, x, y = best_move_list[0]
            # print statements for debugging
            # print(best_move_list)
            # print(x, y)
        #Send your move to the server. Send (x,y) = (-1,-1) to tell the server you have no hand to play
        game_socket.send(pickle.dumps([x,y]))
        
def mini_max(next_moves, turn):
    for i in range(0, len(next_moves)):
        # if next move is along the walls on the x axis, increase the heuristic value 
        if next_moves[i][1] == 0 or next_moves[i][1] == 7: 
            next_moves[i] = (next_moves[i][0] * 10, next_moves[i][1], next_moves[i][2])
        # if next move is along the walls on the y axis, increase the value 
        if next_moves[i][2] == 0 or next_moves[i][2] == 7: 
            next_moves[i] = (next_moves[i][0] * 10, next_moves[i][1], next_moves[i][2])
        # if next move is within the center blocks (i.e. does not give other player a chance at the walls), increase the value
        if turn == 1:
            if (next_moves[i][1] > 1 and next_moves[i][1] < 6) and (next_moves[i][2] > 1 and next_moves[i][2] < 6):
                next_moves[i] = (next_moves[i][0] * 5, next_moves[i][1], next_moves[i][2])
        i += 1

    # need to store a list of possible moves, their outcomes, and weigh them
    return

if __name__ == '__main__':
    main()