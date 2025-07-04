# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *
import importlib.util
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
close_ad_path = os.path.join(current_dir, "../close_ad.air/close_ad.py")
close_ad_module = import_script(close_ad_path)
close_ad_func = getattr(close_ad_module, "close_ad", None)


def get_claims(times=1):
    while True:
      if times >0:
        do_close()
        times=times-1
        print("times")
        print(times)
      else:
        print("times==0")
        break

def do_close():
     touch(Template(r"tpl1748247257220.png", record_pos=(0.078, 0.275), resolution=(720, 1280)))
     if not exists(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600))):
        print("没有空头")
        sleep(2)
        keyevent("back")
        return False
    
     touch(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600)))
     #滚动到底部
     swipe(Template(r"tpl1749723907461.png", record_pos=(-0.384, 0.17), resolution=(900, 1600)), vector=[-0.1264, -0.4531])
     if exists(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)
     if exists(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1751382054859.png", record_pos=(0.287, 0.22), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1751384775354.png", record_pos=(0.284, 0.484), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1751384775354.png", record_pos=(0.284, 0.484), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1751384799594.png", record_pos=(0.289, -0.048), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1751384799594.png", record_pos=(0.289, -0.048), resolution=(900, 1600)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1751119201309.png", record_pos=(0.29, 0.128), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751119201309.png", record_pos=(0.29, 0.128), resolution=(720, 1280)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280))):
                #tweet
                touch(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280)))
                sleep(3)
                stop_app(G.DEVICE.get_top_activity()[0])
     sleep(1)  
     if exists(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280))):
            touch(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280)))
            sleep(9)
#             if exists(Template(r"tpl1749362443543.png", record_pos=(-0.431, -0.797), resolution=(900, 1600))):
#                 print("空头领取成功")
#                 return
            while True:
                
              close_ad_func()
              
              sleep(2)
              if exists(Template(r"tpl1749362443543.png", record_pos=(-0.431, -0.797), resolution=(900, 1600))):
                print("空头领取成功")
                break;
     else:
           if not exists(Template(r"tpl1750213494946.png", record_pos=(0.306, -0.796), resolution=(900, 1600))):
              if exists(Template(r"tpl1749108234200.png", record_pos=(0.347, -0.856), resolution=(720, 1280))):
                 touch(Template(r"tpl1749108245783.png", record_pos=(0.457, -0.853), resolution=(720, 1280)))
              if exists(Template(r"tpl1749395723999.png", record_pos=(0.362, -0.841), resolution=(900, 1600))):
                 touch(Template(r"tpl1749395730238.png", record_pos=(0.446, -0.841), resolution=(900, 1600)))
              print("app启动")
           do_close()
    
     return True

# get_claims(1);
# close_ad_func()











