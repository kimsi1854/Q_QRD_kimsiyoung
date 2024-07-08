import os
from random import sample
from time import sleep
from board import Board
from random_bot import Random_Bot
from player import Player
from Q import QLearningPlayer

board = Board()
ql_player = QLearningPlayer(board, "Q1")
random_bot = Random_Bot(board, "B1")
players = [ql_player, random_bot]
training_games = 30


board.quoridors(training_games, players, print_board=False)
ql_player.save_q_table("q_table.pkl")

# 테스트
board = Board()
test_ql_player = QLearningPlayer(board, "Q1")
test_ql_player.load_q_table("q_table.pkl")
random_bot = Random_Bot(board, "B1")
players = [test_ql_player, random_bot]
test_games = 10

board.quoridors(test_games, players, print_board=True)
print("[{}  {} : {}  {}]".format(players[0].name, players[0].score, players[1].score, players[1].name))

