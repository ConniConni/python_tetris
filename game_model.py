import random

class GameModel:
    def __init__(self):
        # フィールド設定
        self.width = 10
        self.height = 20
        self.field = [[0] * self.width for _ in range(self.height)]

        # ブロック定義
        self.blocks = {
            "I": [(0, 1), (1, 1), (2, 1), (3, 1)],
            "O": [(0, 0), (1, 0), (0, 1), (1, 1)],
            "T": [(0, 1), (1, 0), (1, 1), (1, 2)],
            "Z": [(0, 1), (0, 2), (1, 0), (1, 1)],
            "S": [(0, 0), (0, 1), (1, 1), (1, 2)],
            "L": [(0, 0), (1, 0), (1, 1), (1, 2)],
            "J": [(0, 2), (1, 0), (1, 1), (1, 2)],
        }

        # ゲーム状態
        self.current_block = None
        self.game_over = False

    def spawn_block(self):
        """新しいブロックを生成"""
        block_type = random.choice(list(self.blocks.keys()))
        print(f"block_type:{block_type}")
        self.current_block = self.blocks[block_type]
        self.current_position = (4, 0)
        # check_collision = Trueならば、game_overフラグを立てる
        if self.check_collision(self.current_block, self.current_position):
            self.game_over = True

    def move_block(self, dx, dy):
        """ブロックを移動"""
        # 移動先の座標を定義
        new_position = (self.current_position[0] + dx, self.current_position[1] + dy)
        # check_collision = Falseならば、現在の座標位置を移動先に更新
        if not self.check_collision(self.current_block, new_position):
            self.current_position = new_position
            return True
        return False

    def check_collision(self, block , position):
        """ブロックの衝突判定"""
        # 引数positionから座標を取得
        px, py = position
        # ブロックの座標分の移動が可能か確認
        for dx, dy in block:
            x, y = px + dx, py + dy
            if (
                x < 0
                or x >= self.width
                or y >= self.height
                or (y >= 0 and self.field[y][x] != 0)
            ):
                return True
        return False

    def fix_block(self):
        """ブロックを固定"""
        # 現在の座標位置を取得する
        px, py = self.current_position
        # ブロックが現在の座標位置へ移動可能か判定
        for dx, dy in self.current_block:
            x, y = px + dx, py + dy
            if 0 <= y < self.height:
                self.field[y][x] = 1