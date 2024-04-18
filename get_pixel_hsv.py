import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import colorsys


# RGB到HSV的转换函数
def rgb_to_hsv(rgb):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return hsv


# 显示图片并捕获鼠标点击事件
def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        if 0 <= x < image.width and 0 <= y < image.height:
            # pixel_rgb = image.getpixel((x, y))
            # print(f"像素({x}, {y})的RGB值为: {pixel_rgb}")
            pixel_rgb = pixels[y, x]
            pixel_hsv = rgb_to_hsv(pixel_rgb)
            print(f"像素({x}, {y})的RGB值为: {pixel_rgb}")
            print(f"像素({x}, {y})的HSV值为: {pixel_hsv}")
        else:
            print("点击的像素超出了图片的范围！")


if __name__ == '__main__':
    # 打开图片文件
    image_path = 'pics2/2342024-04-18 16_44_116.png'
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')
    pixels = np.array(rgb_image)

    # 显示图片
    plt.figure()
    plt.imshow(image)
    plt.title('Click on an image pixel to get its RGB and HSV values')
    plt.connect('button_press_event', on_click)
    plt.show()
