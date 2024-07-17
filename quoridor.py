import os
from random import sample
from time import sleep
from board import Board
from Q import QLearningPlayer

training_games = 30
test_games = 10

# 학습
board = Board()
ql_player1 = QLearningPlayer(board, "Q1", alpha=0.1)
ql_player2 = QLearningPlayer(board, "Q2", alpha=0.05)
players = [ql_player1, ql_player2]

board.quoridors(training_games, players, print_board=False)

q_table_q1 = ql_player1.export_q_table()
q_table_q2 = ql_player2.export_q_table()

# 테스트
board = Board()
test_ql_player1 = QLearningPlayer(board, "Q1", alpha=0.1)
test_ql_player2 = QLearningPlayer(board, "Q2", alpha=0.05)

test_ql_player1.import_q_table(q_table_q1)
test_ql_player2.import_q_table(q_table_q2)
players = [test_ql_player1, test_ql_player2]

board.quoridors(test_games, players, print_board=True)
print("[{}  {} : {}  {}]".format(players[0].name, players[0].score, players[1].score, players[1].name))
