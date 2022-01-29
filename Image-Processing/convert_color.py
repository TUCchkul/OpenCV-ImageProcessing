import cv2
image=cv2.imread(r'md.jpg', 1)
image=cv2.cvtColor(src=image, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()