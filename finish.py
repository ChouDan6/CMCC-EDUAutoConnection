import subprocess
import time
import pyautogui
from PIL import ImageGrab
from PIL import Image


def connect_to_cmcc_edu():
    ssid = "CMCC-EDU"  # 替换为实际的 SSID

    command = f"netsh wlan connect name=\"{ssid}\""
    subprocess.run(command, shell=True)
    print("已连接到 WLAN")


def find_and_click_login_button(image_path):
    # 读取登录按钮图像
    login_button_image = Image.open(image_path)

    while True:
        screenshot = ImageGrab.grab()
        location = pyautogui.locate(login_button_image, screenshot, grayscale=True)

        if location is not None:
            x, y = pyautogui.center(location)
            pyautogui.click(x, y)
            break
        else:
            time.sleep(1)  # 如果未找到按钮，等待一秒继续尝试


if __name__ == "__main__":
    connect_to_cmcc_edu()

    # 等待3秒，确保网络连接完成
    time.sleep(3)

    login_button_image_path = "denglu.png"  # 替换为实际的登录按钮图像路径
    find_and_click_login_button(login_button_image_path)
