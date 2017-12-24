import cv2

im_cloned = cv2.imread("cloned.png", cv2.IMREAD_GRAYSCALE)  # 以灰度图形式读取克隆后的图片
im_mask = cv2.imread("mask.png", cv2.IMREAD_GRAYSCALE)  # 以灰度图形式读取克隆后的图片的mask
it = 200  # 设置迭代次数
# 雅可比迭代法
im_temp = im_cloned.copy()
im_seamless = im_temp.copy()
sigma = []
for i in range(im_cloned.shape[0]):
        for j in range(im_cloned.shape[1]):
            if im_mask[i, j] == 255:
                sigma.append([i, j])
# 平滑克隆区域边沿
for a in range(it):
    for [i, j] in sigma:
        term = 10000
        term = term + im_seamless[i+1, j]+im_seamless[i-1, j]+im_seamless[i, j-1]+im_seamless[i, j+1]
        if im_mask[i-1, j] == 255:
            term = term + im_cloned[i, j]-im_cloned[i-1, j]
        if im_mask[i+1, j] == 255:
            term = term + im_cloned[i, j]-im_cloned[i+1, j]
        if im_mask[i, j+1] == 255:
            term = term + im_cloned[i, j]-im_cloned[i, j+1]
        if im_mask[i, j-1] == 255:
            term = term + im_cloned[i, j]-im_cloned[i, j-1]
        im_temp[i, j] = (term-10000)/4
    im_seamless = im_temp.copy()
    if a % 50 == 0:
        print(a)
# 打印原始克隆后的图片和无缝克隆后的图片
cv2.namedWindow("Naive Cloning", 0)  # 定义一个名为Naive Cloning大小可调节的输出窗口
cv2.namedWindow("Seamless Cloning", 0)  # 定义一个名为Seamless Cloning大小可调节的输出窗口
cv2.imshow("Naive Cloning", im_cloned)
cv2.imshow("Seamless Cloning", im_seamless)
cv2.waitKey(0)
