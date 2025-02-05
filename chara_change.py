import cv2  # opencvの読み込み
import numpy as np  # numpyの読み込み
# 定数
BLUE = 0
GREEN = 1
RED = 2
BLUE_MAGNIFICATION = 0.11
GREEN_MAGNIFIATION = 0.59
RED_MAGNIFICATION = 0.3
FILESIZE = 100
TAKASA = 430
HABA = 998
BAIRITU = 1.7
def compression(gazo, gazo_name):  # 画像サイズを圧縮する関数
  size = os.path.getsize(gazo_name)
  quality = 90
  name = 'asshukugazo.jpg'
  while size > FILESIZE * 1000:
    cv2.imwrite(name, gazo, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    size = os.path.getsize(name)
    quality -= 1
  cv2.imwrite(name, gazo, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
  return name
class img_char():
  def __init__(self, name):
    self.gray_char = [" ", "'", ",", "^", "-", "!", "]",
                      "T", "?", "K", "X", "M", "&", "$", "#", "@"]
    img = cv2.imread(name)  # 画像の読み込み
    h, w = img.shape[:2]  # 縮小した後の画像の縦横の大きさを受け取る
    width = round(w * (TAKASA / h) * BAIRITU)
    if width < HABA:
      self.result = cv2.resize(img, dsize=(width, TAKASA))
    else:
      self.result = cv2.resize(img, dsize=(HABA, TAKASA))
    self.img_name = compression(self.result, name)
    self.height, self.width = self.result.shape[:2]  # 縮小した後の画像の縦横の大きさを受け取る
    self.gray_value = np.zeros((self.height, self.width))
    self.color = np.zeros((self.height, self.width, 3))
    self.gray_char = [" ", "'", ",", "^", "-", "!", "]",
                      "T", "?", "K", "X", "M", "&", "$", "#", "@"]
    self.imgchar = ""

  def color_get(self, imge, gure):
    image = cv2.imread(imge)
    for h in range(self.height):
      for w in range(self.width):
        self.color[h][w][BLUE] = image[h, w, BLUE]
        self.color[h][w][GREEN] = image[h, w, GREEN]
        self.color[h][w][RED] = image[h, w, RED]
        self.gray_value[h][w] = self.color[h][w][RED] * RED_MAGNIFICATION + self.color[h][w][GREEN] * \
            GREEN_MAGNIFIATION + self.color[h][w][BLUE] * BLUE_MAGNIFICATION

  def change_gray_character(self):  # 画像を文字に置き換える関数
    self.imgchar = ""
    for h in range(self.height):
      self.imgchar = self.imgchar + "\n"
      for w in range(self.width):
        divide = 0
        while self.gray_value[h][w] + 16 * divide > 0:
          divide -= 1
        self.imgchar += self.gray_char[divide]

  def compression(self, gazo, gazo_name):  # 画像サイズを圧縮する関数
    size = os.path.getsize(gazo_name)
    quality = 90
    name = 'asshukugazo.jpg'
    while size > FILESIZE * 1000:
      cv2.imwrite(name, gazo, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
      size = os.path.getsize(name)
      quality -= 1
    cv2.imwrite(name, gazo, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    return name
