import cv2
import numpy as np
import colorsys


# 回调函数，用于处理鼠标点击事件
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 当左键按下时
        hsv_value = hsv_image[y, x]  # 获取像素的HSV值
        print(f"点击的像素HSV值: {hsv_value}")


# 读取图片
image_path = 'pics1/2342024-04-18 16_44_021.png'
image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# 显示图片
cv2.imshow('Image', image)

# 设置鼠标点击事件的回调函数
cv2.setMouseCallback('Image', on_mouse_click)

# 等待用户关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
