# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from airtest.aircv import *
import re

try:
    from paddleocr import PaddleOCR
except ImportError:
    print("正在安装PaddleOCR...")
    import os
    os.system("pip install paddleocr")
    from paddleocr import PaddleOCR

# 当作为模块导入时，不要重新设置
if __name__ == "__main__":
    auto_setup(__file__)
    # 确保有设备连接
    try:
        device = G.DEVICE
    except:
        connect_device("android://127.0.0.1:7555")  # 使用你的设备序列号

def verify_words(match_words):
    """根据提供的单词列表，在屏幕上查找并点击对应单词"""
    if not match_words or len(match_words) == 0:
        print("错误: 没有提供要匹配的单词")
        return False
    print(f"需要验证的单词: {match_words}")
    # 截图并保存
    screen = G.DEVICE.snapshot()
    pil_image = cv2_2_pil(screen)
    filename = "D:/kyc/temp/verify.png"
    pil_image.save(filename, quality=99, optimize=True)
    print(f"验证截图保存至: {filename}")
    # OCR识别屏幕上的单词和位置
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    result = ocr.ocr(filename, det=True, cls=False)
    # 存储单词和对应坐标
    word_positions = {}
        # 遍历OCR结果，提取单词和位置
    if result and len(result) > 0 and len(result[0]) > 0:
        for item in result[0]:
            # 检查格式是否正确
            if len(item) == 2 and isinstance(item[0], list) and isinstance(item[1], tuple):
                # 获取坐标和文本信息
                box = item[0]  # 坐标 [[x1,y1], [x2,y1], [x2,y2], [x1,y2]]
                text = item[1][0].strip().lower()  # 文本内容转小写
                confidence = item[1][1]  # 置信度
                # 计算中心点坐标
                center_x = (box[0][0] + box[1][0] + box[2][0] + box[3][0]) / 4
                center_y = (box[0][1] + box[1][1] + box[2][1] + box[3][1]) / 4
                # 如果文本是纯单词且置信度高
                if re.match(r"^[a-zA-Z]+$", text) and confidence > 0.8:
                    word_positions[text] = (center_x, center_y, confidence)
                    # print(f"找到单词: {text}, 中心点: ({center_x}, {center_y}), 置信度: {confidence}")
    print(f"屏幕上识别到 {len(word_positions)} 个单词")
    # 点击匹配的单词
    clicked_words = []
    for word in match_words:
        word = word.lower()  # 转小写比较
        if word in word_positions:
            center_x, center_y, confidence = word_positions[word]
            print(f"点击单词: {word} 在坐标 ({center_x}, {center_y})")
            touch((center_x, center_y))
            clicked_words.append(word)
            sleep(0.5)  # 点击间隔
        else:
            print(f"警告: 未找到单词 '{word}'")
    success = len(clicked_words) == len(match_words)
    if success:
        print("所有单词验证成功!")
    else:
        print(f"验证不完整: 找到 {len(clicked_words)}/{len(match_words)} 个单词")
    return success

# 直接执行时的测试代码
if __name__ == "__main__":
    auto_setup(__file__)
    # 测试单词列表
    test_words = ["drill", "require", "census", "enroll", "cigar", "silk", "muscle", "verb", "sleep", "amount", "victory", "awake"]
    success = verify_words(test_words)
    print(f"验证结果: {'成功' if success else '失败'}")








