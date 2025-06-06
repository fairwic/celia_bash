# -*- encoding=utf8 -*-
__author__ = "admin"
__author__ = "admin"

from airtest.core.api import *
from airtest.aircv import *
import sys
import os
import importlib.util
import pytesseract
try:
    from paddleocr import PaddleOCR
except ImportError:
    print("正在安装PaddleOCR...")
    import os
    os.system("pip install paddleocr")
    from paddleocr import PaddleOCR

# 设置系统默认编码为utf-8
import sys
import io
auto_setup(__file__)

def get_points(account):
    #采集到积分数值
    # 打开原始图片
   # 截图并保存
    screen = G.DEVICE.snapshot()
    pil_image = cv2_2_pil(screen)
    # 时间戳
    timestamp = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = f"D:/kyc/temp_points/{account}_{timestamp}.png"
    pil_image.save(filename, quality=99, optimize=True)
    print(f"截图保存至: {filename}")
    # 裁剪积分区域（左上x, 左上y, 右下x, 右下y）
    crop_box = (10, 200, 700, 380)  # 这里的坐标需要你根据实际图片调整
    cropped_image = pil_image.crop(crop_box)
    # cropped_image = image.crop(crop_box)
    # 可选：保存裁剪后的图片，方便调试
    filename = f'D:/kyc/temp_points/cropped_points_{account}.png'
    cropped_image.save(filename)
#     识别出数字
      # 使用OCR识别
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    re = ocr.ocr(filename, det=True, cls=False)
    print("OCR识别完成")
    print(re)
    points_str = re[0][0][1][0]  # 取到'3,525'
    # points = points_str.replace(',', '')  # 去掉逗号
    print(f"积分数值为: {points_str}")
    # 计入到文件中去
    # 创建一个日期的文件.txt
    filename = f"D:/kyc/points_log/points_{time.strftime('%Y%m%d')}.txt"
    with open(filename, "a") as f:
        f.write("-----------------------")
        f.write(f"{account} 积分数值为: {points_str}\n")
    # 获取当前运行的应用包名
    package = G.DEVICE.get_top_activity()[0]
    # 关闭当前应用
    stop_app(package)
get_points("111")








