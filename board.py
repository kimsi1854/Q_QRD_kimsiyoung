import os
import numpy as np
from random import sample
from time import sleep
from BFS import *

class Board:
    def __init__(self):
        self.rows = 9  # 보드의 행 수
        self.cols = 9  # 보드의 열 수
        self.hwalls = np.zeros((self.rows - 1, self.cols))  # 수평 벽
        self.vwalls = np.zeros((self.rows, self.cols - 1))  # 수직 벽
        self.points = np.zeros((self.rows - 1, self.cols - 1))  # 포인트
        self.symbol = ['♥', '♠']  # 플레이어 심볼
        self.pawn = [[0, 4], [8, 4]]  # 플레이어 위치
        self.nplayer = len(self.pawn)  # 플레이어 수
        self.turn = 0  # 현재 턴
        self.maze = np.zeros((self.rows * 2 + 1, self.cols * 2 + 1))  # 미로
        self.maze[2::2, 2::2] = 1  # 미로 벽 설정
        self.maze[0, :] = 1  # 미로 상단 벽
        self.maze[self.rows * 2, :] = 1  # 미로 하단 벽
        self.maze[:, 0] = 1  # 미로 좌측 벽
        self.maze[:, self.cols * 2] = 1  # 미로 우측 벽
        self.num_walls = [10, 10]  # 각 플레이어의 벽 수
        self.players = None  # 플레이어 초기화

    def initialize(self):
        """보드를 초기 상태로 재설정"""
        self.__init__()

    def quoridors(self, games, players, verbose=False, print_board=False):
        """주어진 수의 게임을 플레이"""
        for i in range(games):
            first = sample(range(1, 3), 1)[0]  # 첫 번째 플레이어를 무작위로 선택
            self.join(players, first)  # 플레이어를 게임에 참여시킴
            while not self.is_finish(verbose):
                os.system('cls')  # 화면을 지움
                self.one_play()  # 한 턴 진행
                if print_board: self.print_board_square()  # 보드 출력
                sleep(1)  # 1초 대기
            self.initialize()  # 보드를 초기화

    def one_play(self):
        """한 턴을 진행"""
        if self.players is not None:
            self.players[self.turn].play()
            self.turn = (self.turn + 1) % 2  # 턴 교체
        else:
            print("No players")

    def join(self, players, first):
        """플레이어를 게임에 참여시키고 말을 설정"""
        if first == 1:
            self.players = [players[0], players[1]]
            self.players[0].set_pawn(1)
            self.players[1].set_pawn(2)
        if first == 2:
            self.players = [players[1], players[0]]
            self.players[0].set_pawn(1)
            self.players[1].set_pawn(2)

    def is_finish(self, verbose=False):
        """게임 종료 여부를 확인"""
        if self.pawn[0][0] >= self.rows - 1:
            if verbose: print(self.symbol[0] + " wins")
            self.players[0].score = self.players[0].score + 1
            return True
        if self.pawn[1][0] <= 0:
            if verbose: print(self.symbol[1] + " wins")
            self.players[1].score = self.players[1].score + 1
            return True
        return False

    def move_player(self, direction, pawn):
        """플레이어를 주어진 방향으로 이동"""
        res = True
        if pawn > 0 and pawn <= self.nplayer:
            if direction == 1:
                res = self.is_down_valid(pawn)
                if res: self.pawn[pawn - 1][0] += 1
            if direction == 2:
                res = self.is_left_valid(pawn)
                if res: self.pawn[pawn - 1][1] -= 1
            if direction == 3:
                res = self.is_up_valid(pawn)
                if res: self.pawn[pawn - 1][0] -= 1
            if direction == 4:
                res = self.is_right_valid(pawn)
                if res: self.pawn[pawn - 1][1] += 1
            if direction == 5:
                res = self.is_down_down_valid(pawn)
                if res: self.pawn[pawn - 1][0] += 2
            if direction == 6:
                res = self.is_left_left_valid(pawn)
                if res: self.pawn[pawn - 1][1] -= 2
            if direction == 7:
                res = self.is_up_up_valid(pawn)
                if res: self.pawn[pawn - 1][0] -= 2
            if direction == 8:
                res = self.is_right_right_valid(pawn)
                if res: self.pawn[pawn - 1][1] += 2
            if direction == 9:
                res = self.is_down_right_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] += 1
                    self.pawn[pawn - 1][1] += 1
            if direction == 10:
                res = self.is_down_left_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] += 1
                    self.pawn[pawn - 1][1] -= 1
            if direction == 11:
                res = self.is_left_down_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] += 1
                    self.pawn[pawn - 1][1] -= 1
            if direction == 12:
                res = self.is_left_up_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] -= 1
                    self.pawn[pawn - 1][1] -= 1
            if direction == 13:
                res = self.is_up_left_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] -= 1
                    self.pawn[pawn - 1][1] -= 1
            if direction == 14:
                res = self.is_up_right_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] -= 1
                    self.pawn[pawn - 1][1] += 1
            if direction == 15:
                res = self.is_right_up_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] -= 1
                    self.pawn[pawn - 1][1] += 1
            if direction == 16:
                res = self.is_right_down_valid(pawn)
                if res:
                    self.pawn[pawn - 1][0] += 1
                    self.pawn[pawn - 1][1] += 1
        else:
            print("Invalid pawn")
        if not res: print("Invalid action")
        return res

    def search_direction(self, pawn):
        """플레이어가 이동할 수 있는 방향을 검색"""
        pos_dir = []
        if self.is_down_valid(pawn): pos_dir.append(1)
        if self.is_left_valid(pawn): pos_dir.append(2)
        if self.is_up_valid(pawn): pos_dir.append(3)
        if self.is_right_valid(pawn): pos_dir.append(4)
        if self.is_down_down_valid(pawn): pos_dir.append(5)
        if self.is_left_left_valid(pawn): pos_dir.append(6)
        if self.is_up_up_valid(pawn): pos_dir.append(7)
        if self.is_right_right_valid(pawn): pos_dir.append(8)
        if self.is_down_right_valid(pawn): pos_dir.append(9)
        if self.is_down_left_valid(pawn): pos_dir.append(10)
        if self.is_left_down_valid(pawn): pos_dir.append(11)
        if self.is_left_up_valid(pawn): pos_dir.append(12)
        if self.is_up_left_valid(pawn): pos_dir.append(13)
        if self.is_up_right_valid(pawn): pos_dir.append(14)
        if self.is_right_up_valid(pawn): pos_dir.append(15)
        if self.is_right_down_valid(pawn): pos_dir.append(16)
        return pos_dir

    """방향 1~4"""
    def is_down_valid(self, pawn):
        """아래 방향으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] >= self.rows - 1: return False
        if self.is_wall_down(pawn): return False
        if self.is_opponent_down(pawn): return False
        return True

    def is_left_valid(self, pawn):
        """왼쪽 방향으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] <= 0: return False
        if self.is_wall_left(pawn): return False
        if self.is_opponent_left(pawn): return False
        return True

    def is_up_valid(self, pawn):
        """위쪽 방향으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] <= 0: return False
        if self.is_wall_up(pawn): return False
        if self.is_opponent_up(pawn): return False
        return True

    def is_right_valid(self, pawn):
        """오른쪽 방향으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] >= self.cols - 1: return False
        if self.is_wall_right(pawn): return False
        if self.is_opponent_right(pawn): return False
        return True

    """방향 5~8"""
    def is_down_down_valid(self, pawn):
        """두 칸 아래로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] >= self.rows - 2: return False
        if self.is_wall_down(pawn): return False
        if self.is_opponent_down(pawn) and not self.is_wall_down_down(pawn): return True
        return False

    def is_left_left_valid(self, pawn):
        """두 칸 왼쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] <= 1: return False
        if self.is_wall_left(pawn): return False
        if self.is_opponent_left(pawn) and not self.is_wall_left_left(pawn): return True
        return False

    def is_up_up_valid(self, pawn):
        """두 칸 위로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] <= 1: return False
        if self.is_wall_up(pawn): return False
        if self.is_opponent_up(pawn) and not self.is_wall_up_up(pawn): return True
        return False

    def is_right_right_valid(self, pawn):
        """두 칸 오른쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] >= self.cols - 2: return False
        if self.is_wall_right(pawn): return False
        if self.is_opponent_right(pawn) and not self.is_wall_right_right(pawn): return True
        return False

    """방향 9~16"""
    def is_down_right_valid(self, pawn):
        """오른쪽 대각선 아래로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] >= self.rows - 1: return False
        if self.is_wall_down(pawn): return False
        if self.pawn[pawn - 1][0] < self.rows - 2:
            if self.pawn[pawn - 1][1] < self.cols - 1:
                if self.is_opponent_down(pawn):
                    if self.is_wall_down_down(pawn) and not self.is_wall_down_right(pawn): return True
        if self.pawn[pawn - 1][0] == self.rows - 2:
            if self.pawn[pawn - 1][1] < self.cols - 1:
                if self.is_opponent_down(pawn):
                    if not self.is_wall_down_right(pawn): return True
        return False

    def is_down_left_valid(self, pawn):
        """왼쪽 대각선 아래로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] >= self.rows - 1: return False
        if self.is_wall_down(pawn): return False
        if self.pawn[pawn - 1][0] < self.rows - 2:
            if self.pawn[pawn - 1][1] > 0:
                if self.is_opponent_down(pawn):
                    if self.is_wall_down_down(pawn) and not self.is_wall_down_left(pawn): return True
        if self.pawn[pawn - 1][0] == self.rows - 2:
            if self.pawn[pawn - 1][1] > 0:
                if self.is_opponent_down(pawn):
                    if not self.is_wall_down_left(pawn): return True
        return False

    def is_left_down_valid(self, pawn):
        """아래쪽 대각선 왼쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] <= 0: return False
        if self.is_wall_left(pawn): return False
        if self.pawn[pawn - 1][1] > 1:
            if self.pawn[pawn - 1][0] < self.rows - 1:
                if self.is_opponent_left(pawn):
                    if self.is_wall_left_left(pawn) and not self.is_wall_left_down(pawn): return True
        if self.pawn[pawn - 1][1] == 1:
            if self.pawn[pawn - 1][0] < self.rows - 1:
                if self.is_opponent_left(pawn):
                    if not self.is_wall_left_down(pawn): return True
        return False

    def is_left_up_valid(self, pawn):
        """위쪽 대각선 왼쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] <= 0: return False
        if self.is_wall_left(pawn): return False
        if self.pawn[pawn - 1][1] > 1:
            if self.pawn[pawn - 1][0] > 0:
                if self.is_opponent_left(pawn):
                    if self.is_wall_left_left(pawn) and not self.is_wall_left_up(pawn): return True
        if self.pawn[pawn - 1][1] == 1:
            if self.pawn[pawn - 1][0] > 0:
                if self.is_opponent_left(pawn):
                    if not self.is_wall_left_up(pawn): return True
        return False

    def is_up_left_valid(self, pawn):
        """왼쪽 대각선 위로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] <= 0: return False
        if self.is_wall_up(pawn): return False
        if self.pawn[pawn - 1][0] > 1:
            if self.pawn[pawn - 1][1] > 0:
                if self.is_opponent_up(pawn):
                    if self.is_wall_up_up(pawn) and not self.is_wall_up_left(pawn): return True
        if self.pawn[pawn - 1][0] == 1:
            if self.pawn[pawn - 1][1] > 0:
                if self.is_opponent_up(pawn):
                    if not self.is_wall_up_left(pawn): return True
        return False

    def is_up_right_valid(self, pawn):
        """오른쪽 대각선 위로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][0] <= 0: return False
        if self.is_wall_up(pawn): return False
        if self.pawn[pawn - 1][0] > 1:
            if self.pawn[pawn - 1][1] < self.cols - 1:
                if self.is_opponent_up(pawn):
                    if self.is_wall_up_up(pawn) and not self.is_wall_up_right(pawn): return True
        if self.pawn[pawn - 1][0] == 1:
            if self.pawn[pawn - 1][1] < self.cols - 1:
                if self.is_opponent_up(pawn):
                    if not self.is_wall_up_right(pawn): return True
        return False

    def is_right_up_valid(self, pawn):
        """위쪽 대각선 오른쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] >= self.cols - 1: return False
        if self.is_wall_right(pawn): return False
        if self.pawn[pawn - 1][1] < self.cols - 2:
            if self.pawn[pawn - 1][0] > 0:
                if self.is_opponent_right(pawn):
                    if self.is_wall_right_right(pawn) and not self.is_wall_right_up(pawn): return True
        if self.pawn[pawn - 1][1] == self.cols - 2:
            if self.pawn[pawn - 1][0] > 0:
                if self.is_opponent_right(pawn):
                    if not self.is_wall_right_up(pawn): return True
        return False

    def is_right_down_valid(self, pawn):
        """아래쪽 대각선 오른쪽으로의 이동이 유효한지 확인"""
        if self.pawn[pawn - 1][1] >= self.cols - 1: return False
        if self.is_wall_right(pawn): return False
        if self.pawn[pawn - 1][1] < self.cols - 2:
            if self.pawn[pawn - 1][0] < self.rows - 1:
                if self.is_opponent_right(pawn):
                    if self.is_wall_right_right(pawn) and not self.is_wall_right_down(pawn): return True
            if self.pawn[pawn - 1][1] == self.cols - 2:
                if self.pawn[pawn - 1][0] < self.rows - 1:
                    if self.is_opponent_right(pawn):
                        if not self.is_wall_right_down(pawn): return True
        return False

    def is_opponent_down(self, pawn):
        """아래에 상대 플레이어가 있는지 확인"""
        if self.pawn[pawn % 2][1] == self.pawn[pawn - 1][1]:
            if self.pawn[pawn % 2][0] == self.pawn[pawn - 1][0] + 1:
                return True
        return False

    def is_opponent_left(self, pawn):
        """왼쪽에 상대 플레이어가 있는지 확인"""
        if self.pawn[pawn % 2][0] == self.pawn[pawn - 1][0]:
            if self.pawn[pawn % 2][1] == self.pawn[pawn - 1][1] - 1:
                return True
        return False

    def is_opponent_up(self, pawn):
        """위에 상대 플레이어가 있는지 확인"""
        if self.pawn[pawn % 2][1] == self.pawn[pawn - 1][1]:
            if self.pawn[pawn % 2][0] == self.pawn[pawn - 1][0] - 1:
                return True
        return False

    def is_opponent_right(self, pawn):
        """오른쪽에 상대 플레이어가 있는지 확인"""
        if self.pawn[pawn % 2][0] == self.pawn[pawn - 1][0]:
            if self.pawn[pawn % 2][1] == self.pawn[pawn - 1][1] + 1:
                return True
        return False

    def is_wall_down(self, pawn):
        """아래쪽에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_left(self, pawn):
        """왼쪽에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1] - 1] == 1: return True
        return False

    def is_wall_up(self, pawn):
        """위쪽에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0] - 1, self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_right(self, pawn):
        """오른쪽에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_down_down(self, pawn):
        """두 칸 아래에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0] + 1, self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_left_left(self, pawn):
        """두 칸 왼쪽에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1] - 2] == 1: return True
        return False

    def is_wall_up_up(self, pawn):
        """두 칸 위에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0] - 2, self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_right_right(self, pawn):
        """두 칸 오른쪽에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1] + 1] == 1: return True
        return False

    def is_wall_down_right(self, pawn):
        """오른쪽 아래에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0] + 1, self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_down_left(self, pawn):
        """왼쪽 아래에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0] + 1, self.pawn[pawn - 1][1] - 1] == 1: return True
        return False

    def is_wall_left_down(self, pawn):
        """왼쪽 아래에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1] - 1] == 1: return True
        return False

    def is_wall_left_up(self, pawn):
        """왼쪽 위에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0] - 1, self.pawn[pawn - 1][1] - 1] == 1: return True
        return False

    def is_wall_up_left(self, pawn):
        """왼쪽 위에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0] - 1, self.pawn[pawn - 1][1] - 1] == 1: return True
        return False

    def is_wall_up_right(self, pawn):
        """오른쪽 위에 벽이 있는지 확인"""
        if self.vwalls[self.pawn[pawn - 1][0] - 1, self.pawn[pawn - 1][1]] == 1: return True
        return False

    def is_wall_right_up(self, pawn):
        """오른쪽 위에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0] - 1, self.pawn[pawn - 1][1] + 1] == 1: return True
        return False

    def is_wall_right_down(self, pawn):
        """오른쪽 아래에 벽이 있는지 확인"""
        if self.hwalls[self.pawn[pawn - 1][0], self.pawn[pawn - 1][1] + 1] == 1: return True
        return False

    def is_player_inboard(self, pawn, bottom, left, up, right):
        """플레이어가 보드 안에 있는지 확인"""
        if self.pawn[pawn - 1][0] <= bottom:
            if self.pawn[pawn - 1][1] >= left:
                if self.pawn[pawn - 1][0] >= up:
                    if self.pawn[pawn - 1][1] <= right: return True
        return False

    def put_wall(self, r, c, direction, pawn):
        """벽을 놓음"""
        if self.num_walls[pawn - 1] <= 0:
            print("{} has no walls.".format(self.players[pawn - 1].name))
            return False
        if self.is_wall_valid(r, c, direction):
            self.num_walls[pawn - 1] -= 1
            if direction == 1:
                self.hwalls[r, c:c + 2] = 1
                self.points[r, c] = 1
            if direction == 2:
                self.vwalls[r:r + 2, c] = 1
                self.points[r, c] = 1
            return True
        else:
            print("Invalid wall.")
            return False

    def is_wall_valid(self, r, c, direction):
        """벽이 유효한지 확인"""
        if r < 0 or r >= self.rows - 1: return False
        if c < 0 or c >= self.cols - 1: return False
        if self.points[r, c] == 1: return False
        if direction == 1:
            if self.hwalls[r, c] == 1 or self.hwalls[r, c + 1] == 1: return False
        if direction == 2:
            if self.vwalls[r, c] == 1 or self.vwalls[r + 1, c] == 1: return False
        if self.is_path_closed(r, c, direction): return False
        return True

    def is_path_closed(self, r, c, direction):
        """벽을 놓았을 때 경로가 막히는지 확인"""
        player1_closed = True
        player2_closed = True
        before_maze = self.maze.copy()  # 현재 미로 상태를 저장
        if direction == 1: self.maze[r * 2 + 2, c * 2 + 1:c * 2 + 4] = 1
        if direction == 2: self.maze[r * 2 + 1:r * 2 + 4, c * 2 + 2] = 1

        for i in range(self.cols):
            start = tuple([self.pawn[0][0] * 2 + 1, self.pawn[0][1] * 2 + 1])
            end = tuple([(self.rows - 1) * 2 + 1, i * 2 + 1])
            if BFS(self.maze, start, end) > 0:
                player1_closed = False
                break

        for i in range(self.cols):
            start = tuple([self.pawn[1][0] * 2 + 1, self.pawn[1][1] * 2 + 1])
            end = tuple([1, i * 2 + 1])
            if BFS(self.maze, start, end) > 0:
                player2_closed = False
                break
        if player1_closed or player2_closed: self.maze = before_maze  # 경로가 막히면 이전 상태로 복원
        return player1_closed or player2_closed

    def print_board_line(self):
        """보드를 라인 형태로 출력"""
        board_s = ''
        for i in range(self.rows):
            for j in range(self.cols):
                board_s = board_s + '□'
                if j < self.cols - 1:
                    if self.vwalls[i, j] == 1: board_s = board_s + ' | '
                    else: board_s = board_s + '   '
                else: board_s = board_s + '\n'
            if i < self.rows - 1:
                for j in range(self.cols):
                    if self.hwalls[i, j] == 1:
                        board_s = board_s + 'ㅡ '
                    else:
                        board_s = board_s + '   '
                    if j < self.cols - 1:
                        if self.points[i, j] == 1: board_s = board_s + '·'
                        else: board_s = board_s + '  '
                board_s = board_s + '\n'
        print(board_s)

    def print_board_square(self):
        """보드를 사각형 형태로 출력"""
        board_s = (self.symbol[0] + ': {} ({} walls) \n' + self.symbol[1] + ': {} ({} walls)\n').format(\
            self.players[0].name, self.num_walls[0], self.players[1].name, self.num_walls[1])
        for i in range(self.rows):
            for j in range(self.cols):
                if i == self.pawn[0][0] and j == self.pawn[0][1]: board_s = board_s + self.symbol[0]
                elif i == self.pawn[1][0] and j == self.pawn[1][1]: board_s = board_s + self.symbol[1]
                else: board_s = board_s + '□'
                if j < self.cols - 1:
                    if self.vwalls[i, j] == 1: board_s = board_s + ' ■ '
                    else: board_s = board_s + '    '
                else: board_s = board_s + '\n'
            if i < self.rows - 1:
                for j in range(self.cols):
                    if self.hwalls[i, j] == 1:
                        board_s = board_s + '■ '
                    else:
                        board_s = board_s + '   '
                    if j < self.cols - 1:
                        if self.points[i, j] == 1: board_s = board_s + '■ '
                        else: board_s = board_s + '   '
                board_s = board_s + '\n'
        print(board_s)

    def print_maze(self):
        """미로를 출력"""
        maze_s = ''
        for i in range(self.maze.shape[0]):
            for j in range(self.maze.shape[1]):
                if i == self.pawn[0][0] * 2 + 1 and j == self.pawn[0][1] * 2 + 1:
                    maze_s = maze_s + self.symbol[0] + ' '
                    continue
                if i == self.pawn[1][0] * 2 + 1 and j == self.pawn[1][1] * 2 + 1:
                    maze_s = maze_s + self.symbol[1] + ' '
                    continue
                if self.maze[i, j] == 1: maze_s = maze_s + '■ '
                else: maze_s = maze_s + '   '
            maze_s = maze_s + '\n'
        print(maze_s)
