from tkinter import Canvas, Button, Label

CELL_SIZE = 30

class GameView:
    def __init__(self, root ,model):
        self.model = model

        # キャンバス
        self.canvas = Canvas(root, width=model.width * CELL_SIZE, height=model.height * CELL_SIZE, bg="black")
        self.canvas.pack(side="left")

        # スコアラベル
        self.score_label = Label(root, text="Score: 0", font=("Arial", 16))
        self.score_label.pack(side="top")

        # ボタン
        self.start_button = Button(root, text="Start")
        self.start_button.pack(side="top")
        self.reset_button = Button(root, text="Reset")
        self.reset_button.pack(side="top")

    def draw_field(self):
        """フィールドと現在のブロックを描画"""
        # キャンバスの初期化
        if not self.model.game_over:
            self.canvas.delete("all")

        # フィールド上の固定ブロックを描画
        for y in range(self.model.height):
            for x in range(self.model.width):
                if self.model.field[y][x] == 1:
                    self.canvas.create_rectangle(
                        x * CELL_SIZE, y * CELL_SIZE,
                        (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                        fill="cyan", outline="gray"
                    )

        # 現在のブロックを描画
        if self.model.current_block:
            px, py = self.model.current_position
            for dx, dy in self.model.current_block:
                x, y = px + dx, py + dy
                self.canvas.create_rectangle(
                    x * CELL_SIZE, y * CELL_SIZE,
                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                    fill="yellow", outline="gray"
                )

    def set_start_button_callback(self, callback):
        """スタートボタンのコールバックを設定"""
        self.start_button.config(command=callback)

    def set_reset_button_callback(self, callback):
        """リセットボタンのコールバックを設定"""
        self.reset_button.config(command=callback)