# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
import sys
import os
import importlib.util
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
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

auto_setup(__file__)

# 确保设备已连接
def connect_to_device(max_retries=3):
    for attempt in range(max_retries):
        try:
            device = G.DEVICE
            print(f"已连接设备: {device}")
            return True
        except:
            print(f"尝试连接设备... 第 {attempt + 1} 次")
            try:
                # 使用正确的连接格式
                connect_device("Android:///127.0.0.1:7555")
                print("设备连接成功！")
                return True
            except Exception as e:
                print(f"连接失败: {str(e)}")
                if attempt < max_retries - 1:
                    print("等待 5 秒后重试...")
                    sleep(5)
                else:
                    print("设备连接失败，请检查以下问题：")
                    print("1. 模拟器是否正在运行")
                    print("2. ADB 端口 7555 是否正确")
                    print("3. ADB 服务是否正常运行")
                    return False

# 尝试连接设备
if not connect_to_device():
    print("程序退出")
    sys.exit(1)

# 改进的导入脚本函数，确保设备上下文传递
def import_script(script_path):
    print(f"导入脚本: {script_path}")
    spec = importlib.util.spec_from_file_location("script", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # 确保导入的模块使用相同的设备实例
    if hasattr(G, 'DEVICE') and G.DEVICE:
        module_globals = getattr(module, 'G', None)
        if module_globals and not hasattr(module_globals, 'DEVICE'):
            setattr(module_globals, 'DEVICE', G.DEVICE)
    
    return module

# 获取脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
find_words_path = os.path.join(current_dir, "find_words.py")
touch_words_path = os.path.join(current_dir, "touch_words.py")

# 优化提取的函数: 返回到挖矿界面
def return_to_mining():
    # 点击返回
    if exists(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412))):
      touch(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412)))
    sleep(1)
    # 点击挖矿
    touch(Template(r"tpl1746071030321.png", record_pos=(-0.359, 0.176), resolution=(540, 960)))
    sleep(2)
    # 点击挖矿开始
    touch(Template(r"tpl1745325233736.png", record_pos=(-0.008, -0.651), resolution=(1176, 2400)))
    sleep(2)

# 优化提取的函数: 重新执行OCR识别
def retry_ocr(find_words, username):
    # 点击返回
    touch(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412)))
    sleep(1)
    # 点击挖矿
    touch(Template(r"tpl1745476843909.png", record_pos=(-0.005, -0.73), resolution=(1080, 2412)))
    sleep(1)
    touch(Template(r"tpl1745477193126.png", record_pos=(0.003, 0.895), resolution=(1080, 2412)))
    sleep(2)
    # 重新执行ocr识别
    words = find_words.get_words(username)
    if words is None or len(words) < 12:
        print(f"账号 {username} ocr识别单词失败!")
        return None
    print(f"成功识别到单词列表: {words}")
    return words

# 优化提取的函数: 执行验证流程
def verify_words_process(touch_words, words):
    # 点击next
    touch(Template(r"tpl1745418012503.png", record_pos=(-0.003, 0.035), resolution=(1080, 2412)))
    sleep(4)
    
    # 执行touch_words验证
    verify_success = touch_words.verify_words(words)
    
    if verify_success:
        print(f"账号 {username} KYC验证成功!")
    else:
        print(f"账号 {username} KYC验证失败!")
        
    # 点击验证完成
    touch(Template(r"tpl1745464859336.png", record_pos=(-0.014, 0.346), resolution=(1080, 2412)))
    sleep(2)
    
    return verify_success

def kyc_ocr(find_words_path, username):
    if exists(Template(r"tpl1745411051315.png", record_pos=(-0.035, 0.892), resolution=(1080, 2412))):
        touch(Template(r"tpl1745411051315.png", record_pos=(-0.035, 0.892), resolution=(1080, 2412)))
        
        # 执行OCR识别，获取单词列表
        sleep(1)
        find_words = import_script(find_words_path)
        words = find_words.get_words(username)
        if words is None:
            print(f"账号 {username} ocr识别单词失败!")
            return
        print(f"成功识别到单词列表: {words}")
        
        # 如果单词列表长度小于12，则判断为有特殊字符太长了，导致换行异常
        if len(words) < 12:
            words = retry_ocr(find_words, username)
            if not words:
                return

        # 执行验证流程
        touch_words = import_script(touch_words_path)
        verify_success = verify_words_process(touch_words, words)
        # 当没有返回到挖矿界面说明，ocr又失败了，重新执行ocr识别
        if not exists(Template(r"tpl1747291181307.png", record_pos=(-0.412, 0.278), resolution=(720, 1280))):
            touch(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412)))
            sleep(1)
            # 重新尝试OCR
            words = retry_ocr(find_words, username)
            if words:
                verify_words_process(touch_words, words)
        # 返回到挖矿界面
        return_to_mining()

accounts = [
#     ("dingxueke1025@gmail.com", "Dingxueke@520"),
#     ("fairwickcelia@gmail.com", "fairwickcelia@520"),
#     ("chaoliushishangfaner@gmail.com", "Fangweicong@520"),
#     ("chaoliushishangfanerbtc@gmail.com", "chaoliushishangfanbtc@gmail.com"),

#     ("dingxueke001@outlook.com", "dingxuke@001"),
#     ("fangweicong1001@outlook.com", "fangweicong1001@520"),
#     ("fangweicong1002@outlook.com", "fangweicong1002@520"),
#     ("fangweicong1003@outlook.com", "fangweicong1003@520"),
#     ("fangweicong1004@outlook.com", "fangweicong1004@520"),

#     ("fangweicong1005@outlook.com", "fangweicong@1005"),
#     ("fangweicong1006@outlook.com", "fangweicong@1006"),
#     ("fangweicong1007@outlook.com", "fangweicong@1007"),
# #     #需要验证邮箱
# #     # ("fangweicong1008@outlook.com", "fangweicong@1008"),
#     ("fangweicong1009@outlook.com", "Fangweicong@1009"),


#     ("fangweicong001@gmail.com", "fangweicong001@520"),
#     ("fangweicong002@gmail.com", "fangweicong002@520"),
#     ("fangweicong003@gmail.com", "fangweicong003@520"),
#     ("fangweicong004@gmail.com", "fangweicong004@520"),
#     ("fangweicong005@gmail.com", "fangweicong005@520"),
#     ("fangweicong006@gmail.com", "fangweicong006@520"),
#     ("fangweicong007@gmail.com", "fangweicong007@520"),
#     ("fangweicong008@gmail.com", "fangweicong008@520"),
    # 继续添加更多账号密码
    # ("jegefec313@magpit.com", "Fangweicong@520"),
    # ("ponoyo3578@daupload.com", "Fangweicong@520"),
    # ("yijebix832@jazipo.com", "Fangweicong@520"),
    # ("jasapoy911@bamsrad.com", "Fangweicong@520"),

    ("selid55081@deusa7.com", "Fangweicong@520"),
    ("doroye5846@daupload.com", "Fangweicong@520"),
    ("katikar837@jazipo.com", "Fangweicong@520"),
    ("womabe5305@inkight.com", "Fangweicong@520"),
    ("lecatix608@hazhab.com", "Fangweicong@520"),
    ("xodila4171@magpit.com", "Fangweicong@520"),
    ("moreki9303@daupload.com", "Fangweicong@520"),
    ("jomol30718@daupload.com", "Fangweicong@520"),
    ("bejim48324@neuraxo.com", "Fangweicong@520"),
    ("repovor207@deusa7.com", "Fangweicong@520"),
]

for username, password in accounts:
    #输出日志
    print(f"开始登录账号: {username}")
    print(f"密码: {password}")
    sleep(2)

    #如果存在skip，则点击skip
    if exists(Template(r"tpl1745326722221.png", record_pos=(0.003, 0.954), resolution=(1176, 2400))):
        touch(Template(r"tpl1745326722221.png", record_pos=(0.003, 0.954), resolution=(1176, 2400)))
    #点击我已有账号
    touch(Template(r"tpl1745324912812.png", record_pos=(-0.012, 0.934), resolution=(1176, 2400)))
    sleep(1)
    #点击输入密码
    touch(Template(r"tpl1746070420217.png", record_pos=(-0.194, -0.22), resolution=(540, 960)))
    text(password)
    #点击输入账号
    touch(Template(r"tpl1745474655620.png", record_pos=(0.419, -0.538), resolution=(1080, 2412)))

    for i in range(40):
        keyevent("67")

    text(username)
    #点击登录
    touch(Template(r"tpl1746070921036.png", record_pos=(-0.006, 0.774), resolution=(540, 960)))

    #等待1秒
    sleep(2)

    #如果提示了是否保存密码，点击不保存
    if exists(Template(r"tpl1745325225896.png", record_pos=(0.002, 0.878), resolution=(1176, 2400))):
        touch(Template(r"tpl1745325225896.png", record_pos=(0.002, 0.878), resolution=(1176, 2400)))

    #进入挖矿界面
    return_to_mining()

    #判断是否要kyc认证
    kyc_ocr(find_words_path, username)


    #如果出现 youre verified ,则点击关闭，，并重新点击挖矿
    if exists(Template(r"tpl1746070734314.png", record_pos=(-0.002, 0.078), resolution=(540, 960))):
        touch(Template(r"tpl1746070741785.png", record_pos=(0.009, 0.794), resolution=(540, 960)))
        touch(Template(r"tpl1746070780815.png", record_pos=(-0.022, -0.569), resolution=(540, 960)))
    #广告判断
    #如果没有识别到挖矿成功，则表示有广告
    if not exists(Template(r"tpl1746185085005.png", record_pos=(-0.213, -0.137), resolution=(540, 960))):
        sleep(30)
        # 等待10秒广告结束
        touch(Template(r"tpl1746184976411.png", record_pos=(0.444, -0.837), resolution=(540, 960)))
        # 等待20秒广告结束

    if exists(Template(r"tpl1746071273331.png", record_pos=(-0.439, -0.778), resolution=(540, 960))):
        touch(Template(r"tpl1745325279982.png", record_pos=(-0.429, -0.858), resolution=(1176, 2400)))
    
    sleep(1)
    # 点击进行个人中心
    touch(Template(r"tpl1745325286159.png", record_pos=(-0.419, -0.884), resolution=(1176, 2400)))
    
    #配置挖矿时间
    touch(Template(r"tpl1745500502574.png", record_pos=(-0.119, 0.369), resolution=(1080, 2412)))
    sleep(2)
    touch(Template(r"tpl1747291857349.png", record_pos=(-0.26, 0.029), resolution=(720, 1280)))
    sleep(1)
    #完成配置
    touch(Template(r"tpl1745500552334.png", record_pos=(0.001, 0.35), resolution=(1080, 2412)))
    sleep(2)

    
    # 点击退出登录
    touch(Template(r"tpl1746187685059.png", record_pos=(-0.339, 0.85), resolution=(540, 960)))
    sleep(1)
    # 点击确认退出登录
    touch(Template(r"tpl1745410887477.png", record_pos=(-0.001, 0.403), resolution=(1080, 2412)))
    sleep(2)









