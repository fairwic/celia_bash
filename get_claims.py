# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
# 获取当前运行的应用包名
package = G.DEVICE.get_top_activity()[0]


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
close_ad = os.path.join(current_dir, "close_ad.py")


def get_claim(account):
     touch(Template(r"tpl1748247257220.png", record_pos=(0.078, 0.275), resolution=(720, 1280)))
     if exists(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600))):
        touch(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600)))
        #滚动到底部
        swipe(Template(r"tpl1749723907461.png", record_pos=(-0.384, 0.17), resolution=(900, 1600)), vector=[-0.1264, -0.3531])

        #循环点击四次
        
        if exists(Template(r"tpl1749358296726.png", record_pos=(0.284, 0.208), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358302729.png", record_pos=(0.288, 0.21), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
        if exists(Template(r"tpl1749358296726.png", record_pos=(0.284, 0.208), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358302729.png", record_pos=(0.288, 0.21), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")  
        if exists(Template(r"tpl1749358359870.png", record_pos=(0.286, 0.477), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358374825.png", record_pos=(0.284, 0.478), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                
        if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
        
        if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                
        if exists(Template(r"tpl1749723705202.png", record_pos=(0.283, 0.457), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749723705202.png", record_pos=(0.283, 0.457), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                
        if exists(Template(r"tpl1749723762992.png", record_pos=(0.283, 0.076), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749723762992.png", record_pos=(0.283, 0.076), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                 
        if exists(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280))):
                #tweet
                touch(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
        
        if exists(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280))):
            touch(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280)))
          
        while True:
              close_ad()
              sleep(2)
              if exists(Template(r"tpl1749362443543.png", record_pos=(-0.431, -0.797), resolution=(900, 1600))):
                print("空头领取成功")
                break;
     else:
        keyevent("BACK")
     sleep(2)

    
# get_claim("11");
close_ad()
