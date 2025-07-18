# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
# 获取当前运行的应用包名
package = G.DEVICE.get_top_activity()[0]
import importlib.util

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

    
def get_free_points():
    if exists(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280))):
        touch(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280)))
        sleep(2)
        while True:
        #如果不存在倒计时
          if not exists(Template(r"tpl1751386917466.png", record_pos=(-0.108, 0.557), resolution=(900, 1600))):
           #点击广告
           if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
             touch(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280)))
             sleep(5)

             #如何还在这个页面说明卡住了，退出
             if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
               # 关闭当前应用
               stop_app(package)
               return False;
             i=0
             while True:
               close_ad_func();
               i=i+1
               if  exists(Template(r"tpl1751867660211.png", record_pos=(-0.003, 0.742), resolution=(720, 1280))):
                print("有倒计时表示关闭广告成功")
                keyevent("BACK")
                break;
               else:
                if  exists(Template(r"tpl1750265526065.png", record_pos=(0.082, 0.399), resolution=(720, 1280))):
                  print("有倒计时表示关闭广告成功")
                  break;
                if exists(Template(r"tpl1752078291794.png", record_pos=(-0.358, 0.492), resolution=(900, 1600))):
                    start_app(package)
                if i >5:
                  keyevent("BACK")
                  break;  
                
             break;
           else:
            break;
          else:
            sleep(1);
            break;
        keyevent("BACK")
    else:
        # 没有奖励按钮关闭当前应用
        stop_app(package)
        return False;
    return True;

while True:
     if not get_free_points():
         #重新打开应用
         sleep(1)
         start_app(package)
         sleep(10)
         while True:
            if not exists(Template(r"tpl1750265679140.png", record_pos=(0.429, -0.781), resolution=(720, 1280))):
            
              if exists(Template(r"tpl1749108234200.png", record_pos=(0.347, -0.856), resolution=(720, 1280))):
                 touch(Template(r"tpl1750349642483.png", record_pos=(0.431, -0.828), resolution=(720, 1280)))
              if exists(Template(r"tpl1749395723999.png", record_pos=(0.362, -0.841), resolution=(900, 1600))):
                 touch(Template(r"tpl1749395730238.png", record_pos=(0.446, -0.841), resolution=(900, 1600)))
              print("继续等待app启动")
            else:
                print("启动app成功")
                sleep(10)
                break;
     sleep(3)

























