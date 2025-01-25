import random
from collections import deque

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
        self.current_position = (4, 0)
        self.next_blocks = deque()
        while len(self.next_blocks) < 3:
            block_type = random.choice(list(self.blocks.keys()))
            self.next_blocks.append(block_type)
        self.holder_block = None
        self.score = 0
        self.change_block = False
        self.game_over = False

    def spawn_block(self):
        """新しいブロックを生成"""
        # block_type = random.choice(list(self.blocks.keys()))
        # print(f"block_type:{block_type}")
        # self.current_block = self.blocks[block_type]
        self.current_block = self.blocks[self.next_blocks.popleft()]
        self.update_next_blocks()
        self.current_position = (4, 0)
        self.change_block = False
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

    def rotate_block(self):
        """ブロックを回転"""
        # ブロックを時計回りに90度回転させる
        rotated_block =[(-y, x) for x, y in self.current_block]
        if not self.check_collision(rotated_block, self.current_position):
            self.current_block = rotated_block
            print("rotate_block 90 degrees clockwise")

    def hold_block(self):
        """現在のブロックをホールド"""
        if self.holder_block is None:
            self.change_block = True # 次のブロックが出現するまでブロックの入れ替えを禁止
            self.holder_block = self.current_block
            self.current_block = self.blocks[self.next_blocks.popleft()]
            self.update_next_blocks()
            self.current_position = (4, 0)
            print("hold_block")
        else:
            self.change_block = True # 次のブロックが出現するまでブロックの入れ替えを禁止
            self.current_block, self.holder_block = self.holder_block, self.current_block
            self.current_position = (4, 0)
            print("change_block")

    def check_collision(self, block , position):
        """ブロックの衝突判定"""
        # 引数positionから座標を取得
        px, py = position
        # ブロックの座標分の移動が可能か確認
        if block:
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
        self.clear_lines()

    def clear_lines(self):
        """ラインを消去"""
        # scoreリストを宣言
        score = {1:100, 2:300, 3:500, 4:800}
        # 新しいフィールドを生成。ただし、0を含まない（全て1の）行は除く
        new_field = [row for row in self.field if any(cell == 0 for cell in row)]
        lines_cleared = self.height - len(new_field)
        numbers = int(lines_cleared)
        # 消去ライン数に応じた得点を加算する
        if numbers in score:
            get_score = score[numbers]
            self.score += get_score

            # 新しいフィールドに消去したラインの数だけ、全て値が0の行を追加する
            while len(new_field) < self.height:
                new_field.insert(0, [0] * self.width)
            self.field = new_field

            print(f"add {get_score} point")

    def update_next_blocks(self):
        if not self.game_over:
            while len(self.next_blocks) < 3:
                block_type = random.choice(list(self.blocks.keys()))
                self.next_blocks.append(block_type)
            print(f"next_blocks:[{self.next_blocks[0]},{self.next_blocks[1]},{self.next_blocks[2]}]")
