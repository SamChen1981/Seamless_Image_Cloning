import cv2
import matplotlib.pyplot as plt

im_cloned = cv2.imread("cloned.png", cv2.IMREAD_GRAYSCALE)
im_mask = cv2.imread("mask.png", cv2.IMREAD_GRAYSCALE)
it = 200  # Set number of iterations

im_temp = im_cloned.copy()
im_seamless = im_temp.copy()
sigma = []
for i in range(im_cloned.shape[0]):
        for j in range(im_cloned.shape[1]):
            if im_mask[i, j] == 255:
                sigma.append([i, j])

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

fig, ax = plt.subplots(1, 2)
ax[0].imshow(im_cloned, cmap='gray')
ax[0].set_title('Normal Cloning')
ax[1].imshow(im_seamless, cmap='gray')
ax[1].set_title('Seamless Cloning')

cv2.namedWindow("Naive Cloning", 0)
cv2.namedWindow("Seamless Cloning", 0)

cv2.imshow("Naive Cloning", im_cloned)
cv2.imshow("Seamless Cloning", im_seamless)
cv2.waitKey(0)
