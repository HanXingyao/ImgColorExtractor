import os
import numpy as np
import cv2
import colorsys


def filter_by_hsv(input_image, hsv_lower1, hsv_upper1, hsv_lower2, hsv_upper2):
    """
    根据两个HSV范围过滤图像，并进行腐蚀和膨胀操作。

    参数:
    - input_image: 输入的图像路径或PIL图像对象。
    - hsv_lower1, hsv_upper1: 第一个HSV范围下界和上界。
    - hsv_lower2, hsv_upper2: 第二个HSV范围下界和上界。

    返回:
    - output_image: 输出的PIL图像对象。
    """

    # 如果输入是图像路径，则读取图像
    if isinstance(input_image, str):
        input_image = cv2.imread(input_image)
        # input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    # 将图像转换为HSV模式
    hsv_image = cv2.cvtColor(input_image, cv2.COLOR_RGB2HSV)

    # 创建两个掩码
    mask1 = cv2.inRange(hsv_image, hsv_lower1, hsv_upper1)
    mask2 = cv2.inRange(hsv_image, hsv_lower2, hsv_upper2)

    # 合并两个掩码
    final_mask = cv2.bitwise_or(mask1, mask2)

    # 腐蚀和膨胀
    kernel = np.ones((5, 5), np.uint8)
    mask_eroded = cv2.erode(final_mask, kernel, iterations=1)
    mask_dilated = cv2.dilate(mask_eroded, kernel, iterations=1)

    # 保留原图像中的非黑色部分
    output_image = cv2.bitwise_and(input_image, input_image, mask=mask_dilated)

    return output_image, mask_dilated


# 输入和输出文件夹路径
input_folder = 'pics1'  # 输入的图片文件夹
output_folder = 'pics4'  # 处理后的图片文件夹

# 黄色
hsv_lower = (25, 200, 70)  # HSV下界
hsv_upper = (35, 240, 140)  # HSV上界

# 红色
hsv_lower2 = (170, 240, 55)  # HSV下界
hsv_upper2 = (180, 255, 140)  # HSV上界

# HSV范围
hsv_lower1 = np.array(hsv_lower)  # 第一个HSV范围下界
hsv_upper1 = np.array(hsv_upper)  # 第一个HSV范围上界
hsv_lower2 = np.array(hsv_lower2)  # 第二个HSV范围下界
hsv_upper2 = np.array(hsv_upper2)  # 第二个HSV范围上界

# 如果输出文件夹不存在，则创建它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历输入文件夹中的所有图片文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # 只处理jpg和png格式的图片
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # 过滤图片
            filtered_image, mask = filter_by_hsv(input_path, hsv_lower1, hsv_upper1, hsv_lower2, hsv_upper2)

            # 保存处理后的图像
            cv2.imwrite(output_path, cv2.cvtColor(filtered_image, cv2.COLOR_RGB2BGR))

            # 统计每一列中非黑色像素的数量
            non_black_pixels_count = np.sum(mask, axis=0)

            print(f"文件: {filename}")
            for col, count in enumerate(non_black_pixels_count, start=1):
                print(f"第{col}列非黑色像素数量: {count}")

        except Exception as e:
            print(f"处理失败: {filename}, 错误: {e}")
