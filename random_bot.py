from random import sample, uniform

class Random_Bot:
    def __init__(self, board, name=''):
        self.pawn = None  # 봇의 말을 초기화
        self.board = board  # 게임 보드를 설정
        self.name = name  # 봇의 이름을 설정
        self.score = 0  # 봇의 점수를 초기화

    def set_pawn(self, pawn):
        self.pawn = pawn  # 봇의 말을 설정

    def play(self):
        done = False  # 플레이가 완료되었는지 여부를 추적
        while not done:
            threshold = 0.9  # 이동할지 벽을 놓을지 결정하는 임계값
            if uniform(0,1) <= threshold:
                # 가능한 이동 방향을 검색
                pos_dir = self.board.search_direction(self.pawn)
                if len(pos_dir) > 0:
                    # 가능한 방향 중 하나를 무작위로 선택
                    dir = sample(pos_dir, 1)[0]
                    # 선택된 방향으로 이동을 시도
                    done = self.board.move_player(dir, self.pawn)
            else:
                # 무작위로 벽을 놓을 위치와 방향을 선택
                r = sample(range(self.board.rows), 1)[0]
                c = sample(range(self.board.cols), 1)[0]
                d = sample(range(0, 2), 1)[0] + 1
                # 벽을 놓을 시도를 함
                done = self.wall(r, c, d)

    def move(self, direction):
        # 주어진 방향으로 말을 이동
        res = self.board.move_player(direction, self.pawn)
        return res

    def wall(self, r, c, direction):
        # 주어진 위치와 방향으로 벽을 놓음
        res = self.board.put_wall(r, c, direction, self.pawn)
        return res
