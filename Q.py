import numpy as np
import random

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
                for action in range(1, 17):  # 1~16까지의 행동
                    self.q_table[((r, c), action)] = 0

    def set_pawn(self, pawn):
        self.pawn = pawn

    def choose_action(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(1, 16)  # Exploration: 무작위 행동
        else:
            q_values = [self.q_table[(state, a)] for a in range(1, 17)]
            return np.argmax(q_values) + 1  # Exploitation: 최적 행동 선택

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax([self.q_table[(next_state, a)] for a in range(1, 17)]) + 1
        td_target = reward + self.gamma * self.q_table[(next_state, best_next_action)]
        td_error = td_target - self.q_table[(state, action)]
        self.q_table[(state, action)] += self.alpha * td_error

    def play(self):
        state = (self.board.pawn[self.pawn - 1][0], self.board.pawn[self.pawn - 1][1])
        action = self.choose_action(state)
        valid_move = self.board.move_player(action, self.pawn)
        if valid_move:
            next_state = (self.board.pawn[self.pawn - 1][0], self.board.pawn[self.pawn - 1][1])
            reward = 1 if self.board.is_finish() else 0
            self.update_q_table(state, action, reward, next_state)

    def move(self, direction):
        return self.board.move_player(direction, self.pawn)

    def wall(self, r, c, direction):
        return self.board.put_wall(r, c, direction, self.pawn)
