# -*- encoding=utf8 -*-
__author__ = "admin"

from airtest.core.api import *

auto_setup(__file__)

def close_ad():
     if exists(Template(r"tpl1750337559571.png", record_pos=(0.337, -0.837), resolution=(900, 1600))):
            keyevent("back")
            return
     if exists(Template(r"tpl1749780776910.png", record_pos=(-0.281, 0.629), resolution=(900, 1600))):
            touch(Template(r"tpl1749780776910.png", record_pos=(-0.281, 0.629), resolution=(900, 1600)))
            return 
     if exists(Template(r"tpl1749708765909.png", record_pos=(-0.237, 0.782), resolution=(900, 1600))):
            touch(Template(r"tpl1749708765909.png", record_pos=(-0.237, 0.782), resolution=(900, 1600)))
            return   
     if exists(Template(r"tpl1746184976411.png", record_pos=(0.444, -0.837), resolution=(540, 960))):
            touch(Template(r"tpl1746184976411.png", record_pos=(0.444, -0.837), resolution=(540, 960)))
            return
        # 等待20秒广告结束
     if exists(Template(r"tpl1751375523030.png", record_pos=(-0.235, 0.768), resolution=(720, 1280))):
            touch(Template(r"tpl1751375523030.png", record_pos=(-0.235, 0.768), resolution=(720, 1280)))
            return
        
     elif exists(Template(r"tpl1747885110731.png", record_pos=(0.436, -0.829), resolution=(720, 1280))):
            touch(Template(r"tpl1747885110731.png", record_pos=(0.436, -0.829), resolution=(720, 1280)))
            return
     elif exists(Template(r"tpl1747968753391.png", record_pos=(-0.433, -0.831), resolution=(720, 1280))):
            touch(Template(r"tpl1747968762221.png", record_pos=(-0.433, -0.829), resolution=(720, 1280)))
     elif exists(Template(r"tpl1749031690534.png", record_pos=(-0.438, -0.829), resolution=(720, 1280))):
            touch(Template(r"tpl1749031701656.png", record_pos=(-0.433, -0.828), resolution=(720, 1280)))
            return
     elif exists(Template(r"tpl1749363097708.png", record_pos=(0.456, -0.838), resolution=(900, 1600))):
            touch(Template(r"tpl1749363097708.png", record_pos=(0.456, -0.838), resolution=(900, 1600)))
            return
     elif exists(Template(r"tpl1749364027042.png", record_pos=(0.446, -0.838), resolution=(900, 1600))):
            touch(Template(r"tpl1749364032434.png", record_pos=(0.448, -0.836), resolution=(900, 1600)))
            return
     elif exists(Template(r"tpl1749394747977.png", record_pos=(-0.237, 0.758), resolution=(900, 1600))):
            touch(Template(r"tpl1749394747977.png", record_pos=(-0.237, 0.758), resolution=(900, 1600)))
            return
     elif exists(Template(r"tpl1749898039416.png", record_pos=(0.446, -0.839), resolution=(900, 1600))):
            touch(Template(r"tpl1749898039416.png", record_pos=(0.446, -0.839), resolution=(900, 1600)))
            return
     elif exists(Template(r"tpl1748004705951.png", record_pos=(0.436, -0.829), resolution=(720, 1280))):
            touch(Template(r"tpl1748004735948.png", record_pos=(0.438, -0.822), resolution=(720, 1280)))
            return
     elif exists(Template(r"tpl1750217207644.png", record_pos=(0.442, -0.78), resolution=(900, 1600))):
            keyevent("back")
            sleep(1)
            keyevent("back")
            return
     elif exists(Template(r"tpl1751119280609.png", record_pos=(0.285, 0.821), resolution=(720, 1280))):
            sleep(25)
            sleep(1)
            keyevent("back")
            return
        # 等待10秒广告结束





