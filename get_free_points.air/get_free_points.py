# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
# 获取当前运行的应用包名
package = G.DEVICE.get_top_activity()[0]
def close_ad(count=100):
    if exists(Template(r"tpl1749125040676.png", record_pos=(0.438, -0.826), resolution=(720, 1280))):
      sleep(2);
      touch(Template(r"tpl1749125040676.png", record_pos=(0.438, -0.826), resolution=(720, 1280)))
    elif exists(Template(r"tpl1749104887030.png", record_pos=(0.438, -0.828), resolution=(720, 1280))):
      sleep(2);
      touch(Template(r"tpl1749104887030.png", record_pos=(0.438, -0.828), resolution=(720, 1280)))
      #跳出当前第一个循环
    elif exists(Template(r"tpl1749105310246.png", record_pos=(-0.436, -0.825), resolution=(720, 1280))):
       sleep(2);
       touch(Template(r"tpl1749105310246.png", record_pos=(-0.436, -0.825), resolution=(720, 1280)))
    elif exists(Template(r"tpl1749110709892.png", record_pos=(-0.438, -0.826), resolution=(720, 1280))):
       sleep(2);
       touch(Template(r"tpl1749110709892.png", record_pos=(-0.438, -0.826), resolution=(720, 1280)))
    elif exists(Template(r"tpl1749105692819.png", record_pos=(0.438, -0.828), resolution=(720, 1280))):
      touch(Template(r"tpl1749105692819.png", record_pos=(0.438, -0.828), resolution=(720, 1280)))
    elif exists(Template(r"tpl1749281233102.png", record_pos=(0.444, -0.838), resolution=(900, 1600))):
      touch(Template(r"tpl1749281257543.png", record_pos=(0.444, -0.837), resolution=(900, 1600)))
    
def get_free_points():
    if exists(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280))):
        touch(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280)))
        sleep(2)
        while True:
        #如果不存在倒计时
          if not exists(Template(r"tpl1749280570615.png", record_pos=(-0.094, 0.557), resolution=(900, 1600))):
           #点击广告
           if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
             touch(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280)))
             sleep(3)

             #如何还在这个页面说明卡住了，退出
             if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
               # 关闭当前应用
               stop_app(package)
               return False;

             while True:
               close_ad();
               if  exists(Template(r"tpl1749280595234.png", record_pos=(-0.089, 0.557), resolution=(900, 1600))):
                print("有倒计时表示关闭广告成功")
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
         
         while True:
            if not exists(Template(r"tpl1749620647737.png", record_pos=(-0.428, -0.796), resolution=(900, 1600))):
            
              if exists(Template(r"tpl1749108234200.png", record_pos=(0.347, -0.856), resolution=(720, 1280))):
                 touch(Template(r"tpl1749108245783.png", record_pos=(0.457, -0.853), resolution=(720, 1280)))
              if exists(Template(r"tpl1749395723999.png", record_pos=(0.362, -0.841), resolution=(900, 1600))):
                 touch(Template(r"tpl1749395730238.png", record_pos=(0.446, -0.841), resolution=(900, 1600)))
              print("继续等待app启动")
            else:
                print("启动app成功")
                sleep(20)
                break;
     sleep(3)


















