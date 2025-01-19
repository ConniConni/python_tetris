from tkinter import Tk
from game_model import GameModel
from game_view import GameView
from game_controller import GameController

def main():
    # Tkinter ウィンドウを作成
    root = Tk()
    root.title("Tetris")
    print("make window")

    # ゲームモデル、ビュー、コントローラを初期化
    model = GameModel()
    view = GameView(root,model)
    controller = GameController(model ,view)

if __name__ == "__main__":
    main()