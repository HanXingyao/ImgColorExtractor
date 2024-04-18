import cv2
import numpy as np

# 读取图片
image_path = 'pics1/2342024-04-18 16_44_021.png'
image = cv2.imread(image_path)
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 定义HSV范围
hsv_lower_yellow = np.array([25, 200, 70])
hsv_upper_yellow = np.array([35, 240, 140])

hsv_lower_red = np.array([170, 240, 55])
hsv_upper_red = np.array([180, 255, 140])

# 创建掩码
mask_yellow = cv2.inRange(hsv_image, hsv_lower_yellow, hsv_upper_yellow)
mask_red = cv2.inRange(hsv_image, hsv_lower_red, hsv_upper_red)

# 查找黄色物体的边界
contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours_yellow:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)  # 绘制黄色边界框

# 查找红色物体的边界
contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours_red:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 绘制红色边界框

# 显示图片
cv2.imshow('Detected Objects', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
