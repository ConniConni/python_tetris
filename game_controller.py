CELL_SIZE = 30

class GameController:
    def __init__(self, model , view):
        self.model = model
        self.view = view
        # キャンバスにキーイベントをバインド
        if not self.model.game_over:
            self.view.canvas.bind("<Key>", self.handle_key)
            self.view.canvas.focus_set()

    def start_game(self):
        """ゲームを開始"""
        # 新しいブロックを生成
        self.model.spawn_block()
        self.view.draw_field()
        print("start_game")
        self.game_loop()

    def reset_game(self):
        """ゲームをリセット"""
        self.model.__init__()
        self.view.draw_field()
        print("reset_game")

    def game_loop(self):
        """ゲームループ"""
        if not self.model.move_block(0, 1):
            self.model.fix_block()
            self.model.spawn_block()
            print("move_block available")

        # フィールドと現在のブロックを描画
        self.view.draw_field()
        # スコア表示更新
        self.view.update_score()

        # ゲーム継続判定
        if not self.model.game_over:
            self.view.canvas.after(500, self.game_loop)

        else:
            self.view.canvas.create_text(
                (self.model.width) * CELL_SIZE // 2, self.model.height * CELL_SIZE // 2,
                text="Game OVer", fill="red", font=("Arial", 24)
            )
            print("game_over")
        return

    def handle_key(self, event):
        """キー入力を処理"""
        if event.keysym == "Left":
            self.model.move_block(-1, 0)
        elif event.keysym == "Right":
            self.model.move_block(1, 0)
        elif event.keysym == "Down":
            self.model.move_block(0, 1)
        elif event.keysym == "Up":
            self.model.rotate_block()

        self.view.draw_field()