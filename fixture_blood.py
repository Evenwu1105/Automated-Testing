import pytest
from airtest.core.api import connect_device
#com.sdg.woool.xuezu.huawei包名


@pytest.fixture(scope="module")
def android_device():
    # 连接安卓设备（支持本地USB/远程ADB/模拟器）
    dev = connect_device("Android:///")  # 本地USB连接，也可写 Android://127.0.0.1:5037/设备序列号
    yield dev
    # 测试结束后断开设备
    dev.stop_app("com.sdg.woool.xuezu.huawei")  # 停止被测APP
    dev.disconnect()