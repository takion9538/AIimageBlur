import sys
import numpy as np
import cv2

src = cv2.imread('../Day5/cat.bmp', cv2.IMREAD_GRAYSCALE)

kernel = np.array([[1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9],
                   [1/9, 1/9, 1/9]])

dst = cv2.filter2D(src, -1, kernel)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()