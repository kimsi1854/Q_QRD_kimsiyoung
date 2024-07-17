import numpy as np
import random
from board import Board

class QLearningPlayer:
    def __init__(self, board, name='', alpha=0.1, gamma=0.9, epsilon=0.1):
        self.pawn = None
        self.board = board
        self.name = name
        self.score = 0
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}
        self.init_q_table()

    def init_q_table(self):
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                for action in range(1, 17):
                    self.q_table[((r, c), action)] = 0

    def set_pawn(self, pawn):
        self.pawn = pawn

    def choose_action(self, state, test=False):
        if not test and random.uniform(0, 1) < self.epsilon:
            return random.randint(1, 16)
        else:
            q_values = [self.q_table[(state, a)] for a in range(1, 17)]
            return np.argmax(q_values) + 1

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax([self.q_table[(next_state, a)] for a in range(1, 17)]) + 1
        td_target = reward + self.gamma * self.q_table[(next_state, best_next_action)]
        td_error = td_target - self.q_table[(state, action)]
        self.q_table[(state, action)] += self.alpha * td_error

    def play(self, test=False):
        state = (self.board.pawn[self.pawn - 1][0], self.board.pawn[self.pawn - 1][1])
        action = self.choose_action(state, test)
        valid_move = self.board.move_player(action, self.pawn)
        reward = 0
        if valid_move:
            reward += 0.1  # 유효한 이동
            if self.board.is_opponent_blocked(self.pawn):
                reward += 1  # 상대방을 방해하는 벽 설치
            if self.board.is_finish():
                reward += 0.5  # 게임 승리
            next_state = (self.board.pawn[self.pawn - 1][0], self.board.pawn[self.pawn - 1][1])
            if not test:
                self.update_q_table(state, action, reward, next_state)

    def export_q_table(self):
        return self.q_table

    def import_q_table(self, q_table):
        self.q_table = q_table
