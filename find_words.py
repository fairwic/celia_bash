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
    filename = f"D:/kyc/{account}.png"
    pil_image.save(filename, quality=99, optimize=True)
    print(f"截图保存至: {filename}")
    # 等待1秒
    sleep(1)
    #判断文件是否存在
    if not os.path.exists(filename):
        print(f"文件不存在: {filename}")
        return words

    # 使用OCR识别
    ocr = PaddleOCR(use_angle_cls=True, lang="en")
    result = ocr.ocr(filename, det=True, cls=False)
    print("OCR识别完成")
    

    
    # 如果是标准格式（数字. 单词）
    if result and len(result) > 0 and len(result[0]) > 0:
        # 先尝试直接从结构化数据中提取
        for item in result[0]:
            if len(item) == 2 and isinstance(item[1], tuple) and isinstance(item[1][0], str):
                text = item[1][0].strip()
                # 匹配标准格式 "1. word"
                match = re.match(r"\d+\.\s*(\w+)", text)
                if match:
                    word = match.group(1)
                    words.append(word)
                    print(f"添加单词: {word}")
    # 如果上面的方法提取不到完整12个词，尝试从字符串中提取
    if len(words) < 12:
        print("使用字符串方法提取单词...")
        result_str = str(result)
        matches = re.findall(r"'(\d+\.\s*\w+)'", result_str)
        for match in matches:
            parts = match.split('.', 1)
            if len(parts) == 2:
                word = parts[1].strip()
                if word and word not in words:
                    words.append(word)
                    print(f"添加单词: {word}")
    print("识别到的单词列表:")
    print(words)
    return words

# 直接执行时的测试代码
if __name__ == "__main__":
    auto_setup(__file__)
    words = get_words("test_account")
    print(f"总共识别出 {len(words)} 个单词")
    if len(words) == 12:
        print("识别成功!")
    else:
        print("识别不完整!")






