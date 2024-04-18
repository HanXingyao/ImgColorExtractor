import os
from PIL import Image


# 交换R值和B值的函数
def swap_r_and_b(image_path):
    image = Image.open(image_path)
    rgb_image = image.convert('RGB')
    r, g, b = rgb_image.split()
    return Image.merge('RGB', (b, g, r))


if __name__ == '__main__':
    # 输入和输出文件夹路径
    input_folder = 'pics1'  # 原始图片文件夹
    output_folder = 'pics2'  # 转换后的图片文件夹

    # 如果输出文件夹不存在，则创建它
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有图片文件
    for filename in os.listdir(input_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # 只处理jpg和png格式的图片
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            try:
                # 交换R值和B值，并保存到输出文件夹
                swapped_image = swap_r_and_b(input_path)
                swapped_image.save(output_path)
                print(f"已交换R和B值并保存: {output_path}")
            except Exception as e:
                print(f"处理失败: {filename}, 错误: {e}")
