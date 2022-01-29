import cv2

image=cv2.imread(r'md.jpg', 1)
# thres binary =>pixel=>255:0
#thresh binary =>pixel=>0:255
ret, thresh=cv2.threshold(src=image,thresh=150, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow('image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()