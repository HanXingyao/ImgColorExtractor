import matplotlib.pyplot as plt
from PIL import Image


# 显示图片并捕获鼠标点击事件
def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = int(event.xdata), int(event.ydata)
        if 0 <= x < image.width and 0 <= y < image.height:
            pixel = image.getpixel((x, y))
            print(f"像素({x}, {y})的RGB值为: {pixel}")
        else:
            print("点击的像素超出了图片的范围！")


if __name__ == '__main__':
    # 打开图片文件
    image_path = 'pics1/2342024-04-18 16_44_021.png'
    image = Image.open(image_path)

    # 显示图片
    plt.figure()
    plt.imshow(image)
    plt.title('Click on an image pixel to get its RGB value')
    plt.connect('button_press_event', on_click)
    plt.show()
