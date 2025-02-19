
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget
from shasin import shasinWindow
from doga import dogaWindow
class MainPage(QWidget):
  def __init__(self, stack_widget):
    super().__init__()
    self.stack_widget = stack_widget

    layout = QVBoxLayout()

    # ボタンを作成して、ウィンドウ1に遷移するイベントを設定
    to_window1_button = QPushButton("画像をアスキーにする")
    to_window1_button.clicked.connect(self.goto_window1)

    # ボタンを作成して、ウィンドウ2に遷移するイベントを設定
    to_window2_button = QPushButton("動画をアスキーにする")
    to_window2_button.clicked.connect(self.goto_window2)

    layout.addWidget(to_window1_button)
    layout.addWidget(to_window2_button)
    self.setLayout(layout)

  def goto_window1(self):
    self.stack_widget.setCurrentIndex(1)

  def goto_window2(self):
    self.stack_widget.setCurrentIndex(2)

class MainWindow(QWidget):
  def __init__(self):
    super().__init__()

    # QStackedWidgetを作成
    self.stack_widget = QStackedWidget()

    # 各ページを作成し、スタックウィジェットに追加
    self.main_page = MainPage(self.stack_widget)
    self.window1 = shasinWindow(self.stack_widget)
    self.window2 = dogaWindow(self.stack_widget)

    self.stack_widget.addWidget(self.main_page)
    self.stack_widget.addWidget(self.window1)
    self.stack_widget.addWidget(self.window2)
    main_layout = QVBoxLayout()
    main_layout.addWidget(self.stack_widget)
    self.setLayout(main_layout)

if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec())
