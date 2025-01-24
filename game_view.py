from tkinter import Canvas, Button, Label

CELL_SIZE = 30
SUB_GRID_LENGTH = 4

class GameView:
    def __init__(self, root ,model):
        self.model = model

        # キャンバス
        self.canvas = Canvas(root, width=model.width * CELL_SIZE, height=model.height * CELL_SIZE, bg="black")
        self.canvas.pack(side="left")

        # 次のブロック用のキャンバス
        self.next_canvas = Canvas(
                                    root,
                                    width=SUB_GRID_LENGTH * CELL_SIZE,
                                    height=(model.height - (SUB_GRID_LENGTH - 1)) / SUB_GRID_LENGTH * CELL_SIZE,
                                    bg="gray"
                                )
        self.next_canvas.pack(side="top") #右側に配置

        # 次の次のブロック用のキャンバス
        self.second_canvas = Canvas(
                                    root,
                                    width=SUB_GRID_LENGTH * CELL_SIZE,
                                    height=(model.height - (SUB_GRID_LENGTH - 1)) / SUB_GRID_LENGTH * CELL_SIZE,
                                    bg="gray"
                                    )
        self.second_canvas.pack(side="top") # 右側に配置

        # 次の次の次のブロック用のキャンバス
        self.third_canvas = Canvas(
                                    root,
                                    width=SUB_GRID_LENGTH * CELL_SIZE,
                                    height=(model.height - (SUB_GRID_LENGTH -1)) / SUB_GRID_LENGTH * CELL_SIZE,
                                    bg="gray"
                                    )
        self.third_canvas.pack(side="top") # 右側に配置

        # ホールドブロック用キャンバス
        self.hold_canvas = Canvas(
                                    root,
                                    width=SUB_GRID_LENGTH * CELL_SIZE,
                                    height=(model.height - (SUB_GRID_LENGTH - 1)) / SUB_GRID_LENGTH * CELL_SIZE,
                                    bg="gray"
                                )
        self.hold_canvas.pack(side="top") # 右側に配置

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

    def update_score(self):
        """スコア表示を更新"""
        self.score_label.config(text=f"Score: {self.model.score}")

    def set_start_button_callback(self, callback):
        """スタートボタンのコールバックを設定"""
        self.start_button.config(command=callback)

    def set_reset_button_callback(self, callback):
        """リセットボタンのコールバックを設定"""
        self.reset_button.config(command=callback)