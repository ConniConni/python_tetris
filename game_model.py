class GameModel:
    def __init__(self):
        # フィールド設定
        self.width = 10
        self.height = 20
        self.field = [[0] * self.width for _ in range(self.height)]

        # ゲーム状態
        self.current_block = None
        self.game_over = False