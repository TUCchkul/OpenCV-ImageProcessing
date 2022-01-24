import cv2
image=cv2.imread(filename=r'md.jpg')
cv2.imshow('my pic',image)
cv2.waitKey(10000)
cv2.destryWindows()
