# 导入subprocess模块用于执行命令行命令
import subprocess
import os

# 清理旧的allure结果目录
if os.path.exists("allure-results"):
    subprocess.run("rmdir /s /q allure-results", shell=True)

# 运行pytest测试，使用allure生成测试结果
# --alluredir指定allure结果输出目录
# test_blood.py是要执行的测试文件
subprocess.run("pytest test_blood.py --alluredir=./allure-results", shell=True)

# 生成allure HTML测试报告
# allure-results是测试结果目录
# allure-report是生成的HTML报告目录
# --clean参数会清理旧的报告
subprocess.run("allure generate ./allure-results -o ./allure-report --clean", shell=True)

# 打开allure报告
# 使用allure open命令在浏览器中打开报告
subprocess.run("allure open ./allure-report", shell=True)