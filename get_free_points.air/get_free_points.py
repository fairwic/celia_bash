# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)
# 获取当前运行的应用包名
package = G.DEVICE.get_top_activity()[0]
def close_ad():
   while True:
        #直到发现有关闭按钮或者返回按钮
    if exists(Template(r"tpl1749104887030.png", record_pos=(0.438, -0.828), resolution=(720, 1280))):
      sleep(2);
      touch(Template(r"tpl1749104887030.png", record_pos=(0.438, -0.828), resolution=(720, 1280)))
      #跳出当前第一个循环
      break;
    if exists(Template(r"tpl1749105310246.png", record_pos=(-0.436, -0.825), resolution=(720, 1280))):
       sleep(2);
       touch(Template(r"tpl1749105310246.png", record_pos=(-0.436, -0.825), resolution=(720, 1280)))
       break;
    if exists(Template(r"tpl1749110709892.png", record_pos=(-0.438, -0.826), resolution=(720, 1280))):
       sleep(2);
       touch(Template(r"tpl1749110709892.png", record_pos=(-0.438, -0.826), resolution=(720, 1280)))
       break;
    if exists(Template(r"tpl1749105692819.png", record_pos=(0.438, -0.828), resolution=(720, 1280))):
      sleep(2);
      touch(Template(r"tpl1749105692819.png", record_pos=(0.438, -0.828), resolution=(720, 1280)))
    if exists(Template(r"tpl1749125040676.png", record_pos=(0.438, -0.826), resolution=(720, 1280))):
      sleep(2);
      touch(Template(r"tpl1749125040676.png", record_pos=(0.438, -0.826), resolution=(720, 1280)))
    print("继续循环等待关闭广告")
    #继续循环
    if  exists(Template(r"tpl1749105441372.png", record_pos=(-0.071, 0.571), resolution=(720, 1280))):
        print("出bug了卡住了");
        keyevent("back");
        break;
    sleep(1);
   print("广告关闭结束")

def get_free_points():
    if exists(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280))):
        sleep(2)
        touch(Template(r"tpl1749104758630.png", record_pos=(-0.174, -0.81), resolution=(720, 1280)))
        while True:
        #如果不存在倒计时
          if not exists(Template(r"tpl1749105441372.png", record_pos=(-0.071, 0.571), resolution=(720, 1280))):
           #点击广告
           if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
             touch(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280)))
             sleep(1)

             #如何还在这个页面说明卡住了，退出
             if exists(Template(r"tpl1749104784991.png", record_pos=(-0.01, 0.74), resolution=(720, 1280))):
               # 关闭当前应用
               stop_app(package)
               return False;

             close_ad();
             # 判断是否有倒计时 ，如果没有倒计时 说明关闭广告失败了，重新关闭广告
             if not exists(Template(r"tpl1749105441372.png", record_pos=(-0.071, 0.571), resolution=(720, 1280))):
              print("没有倒计时表示关闭广告失败，重新关闭广告")
              close_ad();
             keyevent("BACK")
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
         sleep(15)
         if exists(Template(r"tpl1749108234200.png", record_pos=(0.347, -0.856), resolution=(720, 1280))):
          touch(Template(r"tpl1749108245783.png", record_pos=(0.457, -0.853), resolution=(720, 1280)))
     sleep(3)












