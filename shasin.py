import sys
import PySide6.QtWidgets as Qw
import PySide6.QtCore as Qc
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog, QVBoxLayout, QPushButton, QWidget, QSizePolicy
from PySide6.QtGui import QPixmap, QFont
from chara_change import img_char
import cv2
import numpy as np
# レイアウト設定用変数
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

sp_exp = Qw.QSizePolicy.Policy.Expanding

def imread(filename, flags=cv2.IMREAD_UNCHANGED, dtype=np.uint8):
  try:
    n = np.fromfile(filename, dtype)
    img = cv2.imdecode(n, flags)
    return img
  except Exception as e:
    print(e)
    return None
class MainWindow(Qw.QMainWindow):

  # コンストラクタ(初期化)

  def __init__(self):

    super().__init__()
    self.fixed_size = Qc.QSize(200, 200)
    self.img_name = ""
    self.setWindowTitle('アスキー画像作成プログラム')
    rect = Qc.QRect()  # Rect: Rectangle (長方形・矩形)
    rect.setSize(Qc.QSize(640, 480))      # サイズ設定
    rect.moveCenter(Qc.QPoint(600, 350))  # 位置設定

    self.setGeometry(rect)

    # メインレイアウトの設定
    central_widget = Qw.QWidget(self)
    self.setCentralWidget(central_widget)
    main_layout = Qw.QVBoxLayout(central_widget)  # 垂直レイアウト

    # QLabelを作成して画像を表示
    self.image_label = QLabel(self)
    self.image_label.setAlignment(Qt.AlignCenter)  # 画像を中央に配置
    main_layout.addWidget(self.image_label)
    self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    # ボタン配置の水平レイアウトを作成します。
    button_layout = Qw.QHBoxLayout()
    button_layout.setAlignment(Qc.Qt.AlignmentFlag.AlignLeft)  # 左寄せ
    main_layout.addLayout(button_layout)  # メインレイアウトにボタンレイアウトを追加

    # 「実行」ボタンの生成と設定
    self.btn_run = Qw.QPushButton('画像ファイルを開く')
    self.btn_run.setMinimumSize(50, 20)
    self.btn_run.setMaximumSize(100, 20)
    self.btn_run.setSizePolicy(sp_exp, sp_exp)
    button_layout.addWidget(self.btn_run)
    self.btn_run.clicked.connect(self.image_get)

    # 「クリア」ボタンの生成と設定
    self.btn_change = Qw.QPushButton('アスキ-に変換')
    self.btn_change.setMinimumSize(100, 20)
    self.btn_change.setMaximumSize(200, 20)
    self.btn_change.setSizePolicy(sp_exp, sp_exp)
    button_layout.addWidget(self.btn_change)

    self.btn_change.clicked.connect(self.image_change)

    # ステータスバー
    self.sb_status = Qw.QStatusBar()
    self.setStatusBar(self.sb_status)
    self.sb_status.setSizeGripEnabled(False)
    self.sb_status.showMessage('プログラムを起動しました。')

  def image_get(self):
    file_name, _ = QFileDialog.getOpenFileName(
        self, "画像を選択", "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)")

    if file_name:
      # 画像をロードして表示

      pixmap = QPixmap(file_name)
      scaled_pixmap = pixmap.scaled(
          self.fixed_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
      self.image_label.setPixmap(scaled_pixmap)
    self.img_name = file_name

  def image_change(self):
    chg = img_char(self.img_name)
    chg.color_get()
    chg.change_gray_character()
    self.image_label.clear()
    self.image_label.setStyleSheet(
        "color: black; font-size: 2px;font-family:'Courier'")

    self.image_label.setText(chg.imgchar)


# 本体
if __name__ == '__main__':
  app = Qw.QApplication(sys.argv)
  main_window = MainWindow()
  main_window.showMaximized()
  main_window.show()
  sys.exit(app.exec())
