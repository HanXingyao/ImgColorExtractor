import os
from PIL import Image
import colorsys


def filter_by_hsv(input_image, hsv_lower, hsv_upper, hsv_lower2, hsv_upper2):
    """
    根据HSV范围过滤图像。

    参数:
    - input_image: 输入的图像路径或PIL图像对象。
    - hsv_lower: HSV下界，格式为 (H_min, S_min, V_min)。
    - hsv_upper: HSV上界，格式为 (H_max, S_max, V_max)。

    返回:
    - output_image: 输出的PIL图像对象。
    """

    # 如果输入是图像路径，则打开图像
    if isinstance(input_image, str):
        input_image = Image.open(input_image)

    # 将图像转换为RGB模式
    rgb_image = input_image.convert('RGB')

    # 初始化输出图像
    output_image = Image.new('RGB', rgb_image.size)

    # 获取图像的像素数据
    pixels = rgb_image.load()

    # 对每个像素进行HSV转换和过滤处理
    for i in range(rgb_image.size[0]):
        for j in range(rgb_image.size[1]):
            r, g, b = pixels[i, j]
            h, s, v = colorsys.rgb_to_hsv(r/255.0, g/255.0, b/255.0)

            # 判断像素是否在HSV范围内
            if ((hsv_lower[0] <= h <= hsv_upper[0] and
                hsv_lower[1] <= s <= hsv_upper[1] and
                hsv_lower[2] <= v <= hsv_upper[2]) or
                (hsv_lower2[0] <= h <= hsv_upper2[0] and
                hsv_lower2[1] <= s <= hsv_upper2[1] and
                hsv_lower2[2] <= v <= hsv_upper2[2])):
                output_image.putpixel((i, j), (r, g, b))  # 保持原颜色
            else:
                output_image.putpixel((i, j), (0, 0, 0))  # 输出黑色

    return output_image


if __name__ == '__main__':
    # 输入和输出文件夹路径
    input_folder = 'pics2'  # 输入的图片文件夹
    output_folder = 'pics3'  # 处理后的图片文件夹

    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 黄色
    hsv_lower = (0.15, 0.85, 0.2)  # HSV下界
    hsv_upper = (0.20, 1.0, 0.5)  # HSV上界

    # 红色
    hsv_lower2 = (0.95, 0.95, 0.2)  # HSV下界
    hsv_upper2 = (1.0, 1.0, 0.5)  # HSV上界

    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # 只处理jpg和png格式的图片
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # 过滤图片并保存到输出文件夹
                filtered_image = filter_by_hsv(input_path, hsv_lower, hsv_upper, hsv_lower2, hsv_upper2)
                # filtered_image.show()  # 显示二值图像
                filtered_image.save(output_path)
                print(f"已处理并保存: {output_path}")
            except Exception as e:
                print(f"处理失败: {filename}, 错误: {e}")