from tkinter import Canvas, Button

CELL_SIZE = 30

class GameView:
    def __init__(self, root ,model):
        self.model = model

        # キャンバス
        self.canvas = Canvas(root, width=model.width * CELL_SIZE, height=model.height * CELL_SIZE, bg="black")
        self.canvas.pack(side="left")

        # ボタン
        self.start_button = Button(root, text="Start")
        self.canvas.pack(side="top")
        self.reset_button = Button(root, text="Reset")
        self.reset_button.pack(side="top")