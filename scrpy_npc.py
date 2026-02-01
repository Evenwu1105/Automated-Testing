from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv

# ---------------------- 仅需修改这3个配置项 ----------------------
# 你要爬取的列表页面URL（比如https://xxx.com/list）
TARGET_URL = "https://aioncodex.com/cn/npcs/light/"
# 总页数
MAX_PAGE = 1
# 下一页按钮的定位（如果下面的默认值不行，按F12改）
# ----------------------------------------------------------------

# 配置Selenium，连接已打开的调试模式Edge窗口
edge_options = Options()
edge_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# 启动浏览器（接管已有窗口，无驱动启动问题）
driver = webdriver.Edge(options=edge_options)

# 存储所有爬取的数据
all_data = []

try:
    # 跳转到爬取页面（已登录状态）
    driver.get(TARGET_URL)
    print("请在浏览器中手动完成验证码，完成后按回车继续...")
    input()  # 等待手动完成验证码

    for page in range(1, MAX_PAGE + 1):
        print(f"\n========== 正在爬取第 {page} 页 ==========")

        # 等待表格加载完成（最多等30秒）
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        # 解析当前页表格数据
        table = driver.find_element(By.TAG_NAME, "table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # 跳过表头，提取每行数据
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 6:
                item_data = {
                    "ID": cols[0].text.strip(),
                    "物品名称": cols[2].text.strip(),  # 名称在第3列
                    "等级": cols[3].text.strip(),
                    "生命力": cols[4].text.strip(),
                    "Grade": cols[5].text.strip()
                }
                all_data.append(item_data)
                print(item_data)

        print(f"第 {page} 页爬取完成，累计数据：{len(all_data)} 条")

        # 非最后一页则点击下一页
        if page < MAX_PAGE:
            try:
                # 等待下一页按钮可点击
                next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="NpcTable_next"]/a')))
                next_btn.click()
                # 随机延时1-3秒，模拟人类操作，避免反爬
                delay = random.uniform(1, 3)
                time.sleep(delay)
            except Exception as e:
                print(f"❌ 第 {page} 页点击下一页失败：{e}")
                print("建议手动点击下一页后，按回车键继续...")
                input()  # 手动操作后按回车继续爬取

except Exception as e:
    print(f"\n❌ 爬取过程出错：{e}")

finally:
    # 关闭浏览器（可选，也可以手动关）
    driver.quit()
    print("\n浏览器已关闭")

# 保存数据到CSV（Excel打开不乱码）
# if all_data:
#     with open("test1.csv", "w", encoding="utf-8-sig", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=["ID", "物品名称", "等级", "生命力", "Grade"])
#         writer.writeheader()
#         writer.writerows(all_data)
#     print(f"✅ 所有数据已保存到「test1.csv」，共 {len(all_data)} 条")
# else:
#     print("❌ 未爬取到任何数据，请检查页面URL或下一页按钮定位")