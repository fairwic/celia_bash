# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
from airtest.aircv import *
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

get_claims = getattr(import_script(os.path.join(current_dir, "./get_claims.air/get_claims.py")), "get_claims", None)

close_ad  = getattr(import_script(os.path.join(current_dir, "./close_ad.air/close_ad.py")), "close_ad", None)



# 优化提取的函数: 返回到挖矿界面
def return_to_mining():
    # 点击返回
#     if exists(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412))):
#       touch(Template(r"tpl1745476629972.png", record_pos=(-0.431, -0.945), resolution=(1080, 2412)))
    sleep(1)
    # 点击挖矿
    touch(Template(r"tpl1749357938905.png", record_pos=(-0.412, 0.362), resolution=(900, 1600)))
    sleep(1)
    if not exists(Template(r"tpl1748249434384.png", record_pos=(-0.215, -0.139), resolution=(720, 1280))):
      # 点击挖矿开始
      touch(Template(r"tpl1745325233736.png", record_pos=(-0.008, -0.651), resolution=(1176, 2400)))
      sleep(6)
      #如果有广告，关闭广告，再继续点击挖矿

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
    if exists(Template(r"tpl1747656682185.png", record_pos=(-0.05, 0.8), resolution=(720, 1280))):
        touch(Template(r"tpl1747656689498.png", record_pos=(-0.068, 0.796), resolution=(720, 1280)))
        # 执行OCR识别，获取单词列表
        sleep(1)
        find_words = import_script(find_words_path)
        words = find_words.get_words(username)
        if words is None:
            print(f"账号 {username} ocr识别单词失败!")
            return False
        print(f"成功识别到单词列表: {words}")
        
        # 如果单词列表长度小于12，则判断为有特殊字符太长了，导致换行异常
        if len(words) < 12:
            words = retry_ocr(find_words, username)
            if not words:
                return False

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
        return True
    return False

accounts = [
#     ("dingxueke1025@gmail.com", "Dingxueke@520"),
#     ("fairwickcelia@gmail.com", "fairwickcelia@520"),
#     ("chaoliushishangfaner@gmail.com", "Fangweicong@520"),
#     ("chaoliushishangfanerbtc@gmail.com",        "chaoliushishangfanbtc@gmail.com"),
#     ("dingxueke001@outlook.com", "dingxuke@001"),
#     ("fangweicong1001@outlook.com", "fangweicong1001@520"),
#     ("fangweicong1002@outlook.com", "fangweicong1002@520"),
#     ("fangweicong1003@outlook.com", "Fangweicong1003@520"),
#     ("fangweicong1004@outlook.com", "fangweicong1004@520"),
#     ("fangweicong1005@outlook.com", "fangweicong@1005"),
#     ("fangweicong1006@outlook.com", "fangweicong@1006"),
#     ("fangweicong1007@outlook.com", "fangweicong@1007"),
#     ("fangweicong1009@outlook.com", "Fangweicong@1009"),
#     ("fangweicong001@gmail.com", "fangweicong001@520"),
#     ("fangweicong002@gmail.com", "fangweicong002@520"),
#     ("fangweicong003@gmail.com", "fangweicong003@520"),
#     ("fangweicong004@gmail.com", "fangweicong004@520"),
#     ("fangweicong005@gmail.com", "fangweicong005@520"),
#     ("fangweicong006@gmail.com", "fangweicong006@520"),
#     ("fangweicong007@gmail.com", "fangweicong007@520"),
#     ("fangweicong008@gmail.com", "fangweicong008@520"),
    
#     ("jegefec313@magpit.com", "Fangweicong@520"),
#     ("ponoyo3578@daupload.com", "Fangweicong@520"),
#     ("yijebix832@jazipo.com", "Fangweicong@520"),
#     ("jasapoy911@bamsrad.com", "Fangweicong@520"),
#     ("selid55081@deusa7.com", "Fangweicong@520"),
#     ("doroye5846@daupload.com", "Fangweicong@520"),
#     ("katikar837@jazipo.com", "Fangweicong@520"),
#     ("womabe5305@inkight.com", "Fangweicong@520"),
#     ("lecatix608@hazhab.com", "Fangweicong@520"),
#     ("xodila4171@magpit.com", "Fangweicong@520"),
#     ("moreki9303@daupload.com", "Fangweicong@520"),
#     ("jomol30718@daupload.com", "Fangweicong@520"),
#     ("bejim48324@neuraxo.com", "Fangweicong@520"),
#     ("repovor207@deusa7.com", "Fangweicong@520"),
    ("vibajo9124@deusa7.com", "Fangweicong@520"),
    ("nifape9682@magpit.com", "Fangweicong@520"),
    ("famex75907@magpit.com", "Fangweicong@520"),
    ("hosikay163@jazipo.com", "Fangweicong@520"),
    ("masak12502@daupload.com", "Fangweicong@520"),
    ("saboy52131@neuraxo.com", "Fangweicong@520"),
    ("xaxela8839@daupload.com", "Fangweicong@520"),
    ("posajo3690@magpit.com", "Fangweicong@520"),
    ("piwobo5616@neuraxo.com", "Fangweicong@520"),
    ("geviy27225@hazhab.com", "Fangweicong@520"),
    ("tojowab604@ofular.com", "Fangweicong@520"),
    ("henate8884@nomrista.com", "Fangweicong@520"),
    ("camim87364@pricegh.com", "Fangweicong@520"),
    ("joyoje5804@ofular.com", "Fangweicong@520"),
    ("colexo7870@pricegh.com", "Fangweicong@520"),
    ("xaleha4786@pricegh.com", "Fangweicong@520"),
    ("deted90896@dlbazi.com", "Fangweicong@520"),
]

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
        f.write(f"{account} 积分数值为: {points_str}\n")

def mining(username):
    #进入挖矿界面
    return_to_mining()
    #判断是否要kyc认证
    #is_need_kyc = kyc_ocr(find_words_path, username)
    is_need_kyc=True
   #如果出现 youre verified ,则点击关闭，，并重新点击挖矿
    if exists(Template(r"tpl1746070734314.png", record_pos=(-0.002, 0.078), resolution=(540, 960))):
        touch(Template(r"tpl1746070741785.png", record_pos=(0.009, 0.794), resolution=(540, 960)))
        touch(Template(r"tpl1746070780815.png", record_pos=(-0.022, -0.569), resolution=(540, 960)))
    #广告判断
    #如果没有识别到挖矿成功，则表示有广告
    if not exists(Template(r"tpl1746185085005.png", record_pos=(-0.213, -0.137), resolution=(540, 960))):
        sleep(10)
        while True:
            close_ad();
            sleep(1)
            if exists(Template(r"tpl1746185085005.png", record_pos=(-0.213, -0.137), resolution=(540, 960))):
                print("已关闭广告")
                break;
            print("继续循环等待广告关闭")
            sleep(1);
    if exists(Template(r"tpl1746071273331.png", record_pos=(-0.439, -0.778), resolution=(540, 960))):
        touch(Template(r"tpl1745325279982.png", record_pos=(-0.429, -0.858), resolution=(1176, 2400)))
    sleep(1)
    return is_need_kyc


#--------------
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
    touch(Template(r"tpl1749357166891.png", record_pos=(0.361, -0.411), resolution=(900, 1600)))

    for i in range(40):
        keyevent("67")

    text(username)
    #点击登录
    touch(Template(r"tpl1746070921036.png", record_pos=(-0.006, 0.774), resolution=(540, 960)))

    #等待1秒
    sleep(1)

    #如果提示了是否保存密码，点击不保存
#     if exists(Template(r"tpl1745325225896.png", record_pos=(0.002, 0.878), resolution=(1176, 2400))):
#         touch(Template(r"tpl1745325225896.png", record_pos=(0.002, 0.878), resolution=(1176, 2400)))
    #挖矿
    is_need_kyc = mining(username)
    is_need_kyc = False
   
    # 获取积分数值
#     get_points(username)
    # 领取空头
    get_claims(1)
    # 点击进行个人中心
    touch(Template(r"tpl1745325286159.png", record_pos=(-0.419, -0.884), resolution=(1176, 2400)))

    # 如果第一次需要kyc认证，则配置挖矿时间
    if is_need_kyc:
      #配置挖矿时间
      touch(Template(r"tpl1745500502574.png", record_pos=(-0.119, 0.369), resolution=(1080, 2412)))
      sleep(2)
      touch(Template(r"tpl1749362853264.png", record_pos=(-0.248, 0.203), resolution=(900, 1600)))
      sleep(1)
      #完成配置
      touch(Template(r"tpl1749363789085.png", record_pos=(-0.002, 0.384), resolution=(900, 1600)))

    # 点击退出登录
    #滚动到底部
    swipe(Template(r"tpl1749361867468.png", record_pos=(-0.404, 0.566), resolution=(900, 1600)), vector=[-0.1264, -0.2531])
    touch(Template(r"tpl1749361996865.png", record_pos=(-0.407, 0.553), resolution=(900, 1600)))
    sleep(1.5)
    # 点击确认退出登录
    touch(Template(r"tpl1745410887477.png", record_pos=(-0.001, 0.403), resolution=(1080, 2412)))
    sleep(2)














