# -*- encoding=utf8 -*-
__author__ = "admin"
auto_setup(__file__)
from airtest.core.api import *
from airtest.aircv import *
import re
from PIL import Image
import cv2
import numpy as np
import pytesseract
import os

# try:
#     from paddleocr import PaddleOCR
# except ImportError:
#     print("正在安装PaddleOCR...")
#     import os
#     os.system("pip install paddleocr")
#     from paddleocr import PaddleOCR

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
os.environ['TESSDATA_PREFIX'] = r'C:\\Program Files (x86)\\Tesseract-OCR\\tessdata'

device = G.DEVICE

def get_words(account=""):
    """
    识别屏幕上的单词列表
    
    参数:
        account: 账号名称，用于保存图片文件名
    
    返回:
        提取到的单词列表
    """
    # 提取单词
    words = []
    if account == "":
        print("账号不能为空")
        return words
    # 截图并保存
    screen = G.DEVICE.snapshot()
    pil_image = cv2_2_pil(screen)
    # 裁剪屏幕中间区域（中心50%）
    width, height = pil_image.size
    left = width * 0.15
    top = height * 0.35
    right = width * 0.85
    bottom = height * 0.65
    pil_image = pil_image.crop((left, top, right, bottom))
    filename = f"D:/kyc/email/{account}.png"
    # filename = f"D:/kyc/2222.png"
    pil_image.save(filename, quality=99, optimize=True)
    print(f"截图保存至: {filename}")
    # 等待1秒
    sleep(1)
    #判断文件是否存在
    if not os.path.exists(filename):
        print(f"文件不存在: {filename}")
        return words

    # # 读取图片
    # img = cv2.imread(filename)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # 中值滤波去噪
    # blur = cv2.medianBlur(gray, 3)
    # # 自适应二值化
    # thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #                                cv2.THRESH_BINARY, 11, 2)
    # # 腐蚀操作去除小噪点
    # kernel = np.ones((2,2), np.uint8)
    # eroded = cv2.erode(thresh, kernel, iterations=1)
    # # 膨胀操作增强数字特征
    # dilated = cv2.dilate(eroded, kernel, iterations=1)
    # cv2.imwrite(filename, dilated)

    digits = split_and_recognize_digits(filename)
    print(111111111111)
    print(digits)
    # 使用OCR识别
    # ocr = PaddleOCR(use_angle_cls=True, lang='en', ocr_version='PP-OCRv4')
    # result = ocr.ocr(filename, det=True, cls=False)
    # print("OCR识别完成")
    # print(result)

    # # 只保留内容为单个数字的检测框，并按x坐标排序
    # digit_boxes = []
    # for line in result:
    #     for word_info in line:
    #         text = word_info[1][0]
    #         if len(text) == 1 and text.isdigit():
    #             # word_info[0] 是检测框的四个点坐标
    #             x = min([pt[0] for pt in word_info[0]])
    #             digit_boxes.append((x, text))
    # # 按x坐标排序
    # digit_boxes.sort(key=lambda x: x[0])
    # # 提取数字
    # words = [text for x, text in digit_boxes]


    return words

def split_and_recognize_digits(filename, num_digits=6):
    import cv2
    from PIL import Image
    import pytesseract
    import numpy as np

    img = cv2.imread(filename)
    h, w = img.shape[:2]
    # 进一步收紧上下边界，避免切到上方文字
    y1 = int(h * 0.65)
    y2 = int(h * 0.95)
    digit_width = int(w / num_digits * 0.92)
    x_offset = int(w / num_digits * 0.04)

    digits = []
    for i in range(num_digits):
        x1 = int(i * w / num_digits + x_offset)
        x2 = int((i + 1) * w / num_digits - x_offset)
        digit_img = img[y1:y2, x1:x2]
        # # 灰度化
        # gray = cv2.cvtColor(digit_img, cv2.COLOR_BGR2GRAY)
        # # 二值化
        # _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # # 反色
        # binary = cv2.bitwise_not(binary)
        # # 找到所有白色像素的最小外接矩形
        # coords = cv2.findNonZero(binary)
        # if coords is not None:
        #     x, y, w_box, h_box = cv2.boundingRect(coords)
        #     # 直接用二值化图像的ROI
        #     digit_roi = binary[y:y+h_box, x:x+w_box]
        #     # 可选：加边框防止数字太贴边
        #     digit_roi = cv2.copyMakeBorder(digit_roi, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=0)
        # else:
        #     digit_roi = binary
        temp_path = f"D:/kyc/email/digit_{i}.png"
        cv2.imwrite(temp_path, digit_img)
        img_pil = Image.open(temp_path)
        config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(img_pil, config=config).strip()
        digits.append(text if text.isdigit() else "?")
    return digits

# 直接执行时的测试代码
if __name__ == "__main__":
    auto_setup(__file__)
    words = get_words("test_account")
    print(words)
    # print(f"总共识别出 {len(words)} 个单词")
    # if len(words) == 12:
    #     print("识别成功!")
    # else:
    #     print("识别不完整!")

import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext(
    'D:/kyc/email/test_account.png',
    allowlist='0123456789',
    decoder='greedy',
    contrast_ths=0.7,
    adjust_contrast=0.7,
    text_threshold=0.5,
    low_text=0.3,
    link_threshold=0.3
)
print(result)






















































