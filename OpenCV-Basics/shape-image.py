import cv2
image=cv2.imread(filename=r'md.jpg', flags=1)
cv2.imshow('my pic',image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()