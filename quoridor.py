import os
from random import sample
from time import sleep
from board import Board
from player import Player
from random_bot import Random_Bot

# Board 객체 생성
board = Board()

from board import Board
from player import Player
from random_bot import Random_Bot
from Q import QLearningPlayer

board = Board()
players = [QLearningPlayer(board, "Q1"), Random_Bot(board, "B1")]
Games = 10
board.quoridors(Games, players, print_board=True)

print("[{}  {} : {}  {}]".format(players[0].name,players[0].score,players[1].score,players[1].name))


# 두 명의 랜덤 봇 플레이어 생성
# 원래는 한 명은 직접 플레이어(YJ)였지만, 현재는 두 명의 랜덤 봇으로 설정됨
#players = [Random_Bot(board, "B1"), YJ(board)]
players = [Random_Bot(board, "B1"), Random_Bot(board, "B2")]

# # 총 10번의 게임을 진행
# Games = 10
#
# # Quoridor 게임을 시작하고 보드를 출력하도록 설정
# board.quoridors(Games, players, print_board=True)
#
# # 승리 점수 설정 (주석 처리됨)
# # winning_score = 100
#
# # 주석 처리된 루프: 플레이어의 점수가 승리 점수에 도달할 때까지 게임을 진행
# # while players[0].score<winning_score and players[1].score<winning_score:
# #     first = sample(range(1,3),1)[0]  # 첫 번째 플레이어를 랜덤하게 선택
# #     board.join(players, first)  # 선택된 플레이어로 게임 시작
# #     while not board.is_finish(verbose=True):  # 게임이 끝날 때까지 반복
# #         os.system('cls')  # 콘솔 창을 지움 (Windows에서는 'cls', Unix에서는 'clear')
# #         board.one_play()  # 한 턴을 진행
# #         board.print_board_square()  # 현재 보드 상태 출력
# #         print("Score  [{} : {}]".format(players[0].score, players[1].score))  # 현재 점수 출력
# #         #sleep(1)  # 1초 대기 (주석 처리됨)
# #     board.initialize()  # 보드를 초기화하여 다음 게임 준비
# # os.system('cls')  # 콘솔 창을 지움
# print("[{}  {} : {}  {}]".format(players[0].name, players[0].score, players[1].score, players[1].name))  # 최종 점수 출력
