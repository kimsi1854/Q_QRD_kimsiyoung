from board import Board

class Player:
    def __init__(self, board, name=''):
        self.pawn = None  # 플레이어의 말을 초기화
        self.board = board  # 게임 보드를 설정
        self.name = name  # 플레이어의 이름을 설정
        self.score = 0  # 플레이어의 점수를 초기화

    def set_pawn(self, pawn):
        self.pawn = pawn  # 플레이어의 말을 설정

    def play(self):
        """게임에서 승리하는 방법을 정의 (현재는 구현되지 않음)"""
        return

    def move(self, direction):
        # 주어진 방향으로 말을 이동
        res = self.board.move_player(direction, self.pawn)
        return res

    def wall(self, r, c, direction):
        # 주어진 위치와 방향으로 벽을 놓음
        res = self.board.put_wall(r, c, direction, self.pawn)
        return res
