#自动截图
import subprocess
import time
import schedule
from datetime import datetime
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import random

class PhoneAutomation:
    def __init__(self):
        # 初始化时获取ADB路径和资源路径
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ADB_PATH = os.path.join(self.BASE_DIR, "adb", "adb.exe")
        self.RES_DIR = os.path.join(self.BASE_DIR, "res")


    def execute_adb_command(self, command):
        """执行ADB命令

        Args:
            command: ADB命令字符串
        Returns:
            命令执行结果
        """
        command = command.replace("adb", f'"{self.ADB_PATH}"')
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                print(f"✓ 命令执行成功: {command}")
                return result.stdout
            else:
                print(f"✗ 命令执行失败: {command}")
                print(f"错误信息: {result.stderr}")
                return None
        except subprocess.TimeoutExpired:
            print(f"✗ 命令执行超时: {command}")
            return None
        except Exception as e:
            print(f"✗ 命令执行异常: {e}")
            return None

    def connect_game(self):
        print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始唤醒屏幕...")
        # 按电源键唤醒
        self.execute_adb_command("adb shell input keyevent KEYCODE_POWER")
        time.sleep(1)
        # 滑动解锁（从下往上滑动）
        self.execute_adb_command("adb shell input swipe 500 1500 500 500")
        time.sleep(1)
        self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
        sleep(30)
        i=1
        while i:
            try:
                if wait(Template(r"./res/tpl1769435744745.png", record_pos=(-0.017, -0.105), resolution=(2400, 1080))):
                    i=0
            except:
                self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")
                sleep(1)
                self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
                sleep(30)
        touch(Template(r"./res/tpl1769435794541.png", record_pos=(0.225, -0.173), resolution=(2400, 1080)))

    def connect_game_switch01(self):
        self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
        sleep(30)
        i = 1
        while i:
            try:
                if wait(Template(r"./res/tpl1769435744745.png", record_pos=(-0.017, -0.105), resolution=(2400, 1080))):
                    i = 0
            except:
                self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")
                sleep(1)
                self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
                sleep(30)
        touch(Template(r"./res/tpl1769435794541.png", record_pos=(0.225, -0.173), resolution=(2400, 1080)))
        sleep(1)
        touch((1200,744))
        swipe(v1=(1332, 800), v2=(1336, 308), duration=0.7)
        swipe(v1=(1332, 800), v2=(1336, 308), duration=0.7)
        sleep(1)
        touch((1140,646))
        sleep(1)
        touch((1568,900))

    def connect_game_switch02(self):
        self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
        sleep(30)
        i = 1
        while i:
            try:
                if wait(Template(r"./res/tpl1769435744745.png", record_pos=(-0.017, -0.105), resolution=(2400, 1080))):
                    i = 0
            except:
                self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")
                sleep(1)
                self.execute_adb_command("adb shell am start -n com.shengqugames.wod/org.cocos2dx.cpp.AppActivity")
                sleep(30)
        touch(Template(r"./res/tpl1769435794541.png", record_pos=(0.225, -0.173), resolution=(2400, 1080)))
        sleep(1)
        touch((1200,744))
        swipe(v1=(1332, 800), v2=(1336, 308), duration=0.7)
        swipe(v1=(1332, 800), v2=(1336, 308), duration=0.7)
        sleep(1)
        touch((1527,644))
        sleep(1)
        touch((1568,900))


    def do_process(self):
        screenshotName = time.strftime("%Y%m%d%H%M", time.localtime())

        touch(Template(r"./res/tpl1769435820663.png", record_pos=(0.0, 0.12), resolution=(2400, 1080)))

        touch(Template(r"./res/tpl1769435838170.png", record_pos=(0.0, 0.188), resolution=(2400, 1080)))
        sleep(3)
        wait(Template(r"./res/tpl1769435885758.png", record_pos=(0.14, -0.16), resolution=(2400, 1080)))
        touch(Template(r"./res/tpl1769435983815.png", record_pos=(0.232, -0.193), resolution=(2400, 1080)))
        sleep(5)
        #金币
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch((1054,284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        double_click((467, 275))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch((1054,284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName + str(random.randint(0, 99999))}.png")
        sleep(3)
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        sleep(3)
        double_click((473.7, 366.7))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch((1054,284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        sleep(3)
        double_click((473.7, 458.2))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        touch((1054,284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        sleep(3)
        double_click((473.7, 547))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        touch((1054,284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        sleep(3)
        double_click((473.7, 635.5))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch((1054, 284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName + str(random.randint(0, 99999))}.png")
        sleep(3)
        touch(Template(r"./res/tpl1769437694477.png", record_pos=(0.341, -0.192), resolution=(2400, 1080)))
        sleep(3)
        double_click((473.7, 727.2))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(3)
        touch((1054, 284))
        sleep(5)
        self.execute_adb_command(f"adb shell screencap -p /sdcard/{screenshotName+str(random.randint(0, 99999))}.png")
        sleep(2)

    def run_full_task(self):
        try:
            print(f"\n=====================================")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行自动化任务...")
            print(f"=====================================\n")

            # 初始化Airtest（确保设备连接）
            if not cli_setup():
                auto_setup(__file__, logdir=True,
                           devices=["android://127.0.0.1:5037/341627646500122?touch_method=MAXTOUCH&", ])

            # 执行核心流程
            self.connect_game()
            self.do_process()
            self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")

            self.connect_game_switch01()
            self.do_process()
            self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")

            self.connect_game_switch02()
            self.do_process()

            print(f"\n=====================================")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 自动化任务执行完成！")
            print(f"=====================================\n")

        except Exception as e:
            print(f"\n=====================================")
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 任务执行异常: {str(e)}")
            print(f"=====================================\n")
            # 异常时强制停止游戏，避免残留进程
            self.execute_adb_command("adb shell am force-stop com.shengqugames.wod")

# --------------------------
# 定时任务配置
# --------------------------
def setup_schedule():
    """配置定时任务"""
    # 创建自动化实例
    phone_auto = PhoneAutomation()

    # 配置定时规则：每天6点执行（可根据需求修改）
    # 方式1：每天6点执行
    # schedule.every().day.at("06:00").do(phone_auto.run_full_task)

    # 方式2：测试用 - 每分钟执行一次（验证逻辑时用，注释掉方式1）
    # schedule.every(1).minutes.do(phone_auto.run_full_task)
    schedule.every().day.at("01:35").do(phone_auto.run_full_task)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 定时任务已启动，将在每天06:00执行！")
    print(f"提示：按 Ctrl+C 可终止程序\n")

    # 持续轮询定时任务
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每60秒检查一次，降低CPU占用


if __name__ == '__main__':
    # 启动定时任务
    setup_schedule()
