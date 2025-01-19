from tkinter import Canvas

CELL_SIZE = 30

class GameView:
    def __init__(self, root ,model):
        self.model = model

        # キャンバス
        self.canvas = Canvas(root, width=model.width * CELL_SIZE, height=model.height * CELL_SIZE, bg="black")