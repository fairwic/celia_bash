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

def check_error():
      if not exists(Template(r"tpl1749723907461.png", record_pos=(-0.384, 0.17), resolution=(900, 1600))):
            
       if exists(Template(r"tpl1749362443543.png", record_pos=(-0.431, -0.797), resolution=(900, 1600))):
#            说明程序错误了，重新挖矿
           ready_claim(account);
       if exists(Template(r"tpl1752068887952.png", record_pos=(-0.358, 0.494), resolution=(900, 1600))):
         start_app(package)
         sleep(5)
         if exists(Template(r"tpl1749108234200.png", record_pos=(0.347, -0.856), resolution=(720, 1280))):
                 touch(Template(r"tpl1750349642483.png", record_pos=(0.431, -0.828), resolution=(720, 1280)))
         if exists(Template(r"tpl1749395723999.png", record_pos=(0.362, -0.841), resolution=(900, 1600))):
                 touch(Template(r"tpl1749395730238.png", record_pos=(0.446, -0.841), resolution=(900, 1600)))

def ready_claim():     
        touch(Template(r"tpl1748247257220.png", record_pos=(0.078, 0.275), resolution=(720, 1280)))
        if not exists(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600))):
          keyevent("BACK")
          sleep(2)
          return False;
        touch(Template(r"tpl1750237729977.png", record_pos=(-0.244, -0.12), resolution=(900, 1600)))
        #滚动到底部
        swipe(Template(r"tpl1749723907461.png", record_pos=(-0.384, 0.17), resolution=(900, 1600)), vector=[-0.1264, -0.3531])
        return True;

def get_claim(account):
        
        boolean=ready_claim()
        if  boolean == False
         return
        #循环点击四次
        
        if exists(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
                check_error();
        if exists(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
                check_error();           
        if exists(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751903288846.png", record_pos=(0.289, 0.126), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")  
                check_error();
        if exists(Template(r"tpl1751903413594.png", record_pos=(0.287, 0.501), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751903413594.png", record_pos=(0.287, 0.501), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
                check_error();
        if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                check_error();
        if exists(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749358312707.png", record_pos=(0.283, 0.078), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                check_error();
                
        if exists(Template(r"tpl1751903257457.png", record_pos=(0.287, -0.122), resolution=(720, 1280))):
                #follow
                touch(Template(r"tpl1751903257457.png", record_pos=(0.287, -0.122), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
                check_error();
                
        if exists(Template(r"tpl1749723762992.png", record_pos=(0.283, 0.076), resolution=(900, 1600))):
                #follow
                touch(Template(r"tpl1749723762992.png", record_pos=(0.283, 0.076), resolution=(900, 1600)))
                sleep(3)
                keyevent("BACK")
                check_error();
                 
        if exists(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280))):
                #tweet
                touch(Template(r"tpl1748248814043.png", record_pos=(0.301, 0.374), resolution=(720, 1280)))
                sleep(3)
                keyevent("BACK")
                check_error();
        
        if exists(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280))):
            touch(Template(r"tpl1748249041841.png", record_pos=(-0.006, 0.796), resolution=(720, 1280)))
          
        while True:
              close_ad()
              sleep(2)
              if exists(Template(r"tpl1749362443543.png", record_pos=(-0.431, -0.797), resolution=(900, 1600))):
                print("空头领取成功")
                break;
     

    
get_claim("11");
# close_ad()

