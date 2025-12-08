from airtest.core.api import *
from fixture_blood import android_device
import blood


#com.sdg.woool.xuezu.huawei包名

def test_login_success(android_device):
    # 启动APP
    android_device.start_app("com.sdg.woool.xuezu.huawei")
    fontPage = wait(Template(r"./res/tpl1765161019352.png", record_pos=(0.001, 0.609), resolution=(1260, 2720)),timeout=15)
    touch(fontPage)
    wait(Template(r"./res/tpl1765161100977.png", record_pos=(-0.408, 0.92), resolution=(1260, 2720)),timeout=15)

    # 断言：登录成功后是否显示首页元素
    assert exists(Template(r"./res/tpl1765161100977.png", record_pos=(-0.408, 0.92), resolution=(1260, 2720))), "登录失败，未跳转到首页"


def test_battle_success(android_device):
    xz = blood.Xuezu()
    xz.battle()

    assert exists(Template(r"./res/tpl1765099664521.png", record_pos=(0.006, 0.609), resolution=(1260, 2720))),"战斗结束未能回到首页或战斗失败"