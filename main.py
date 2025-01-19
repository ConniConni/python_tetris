from tkinter import Tk
from game_model import GameModel
from game_view import GameView
from game_controller import GameController

def main():
    # Tkinter ウィンドウを作成
    root = Tk()
    root.title("Tetris")

    # ゲームモデル、ビュー、コントローラを初期化
    model = GameModel()
    view = GameView(root,model)
    controller = GameController(model ,view)

    # スタートボタンにコントローラのメソッドを設定
    view.set_start_button_callback(controller.start_game)

    # Tkinter イベントループ開始
    root.mainloop()

if __name__ == "__main__":
    main()