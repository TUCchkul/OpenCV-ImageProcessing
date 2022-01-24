import cv2

#to read an image in colour format which does not include alpha channel=1, cv2.IMREAD_COLOR
# to read an image in grayscale=0, cv2.IMREAD_GRAYSCALE
#to read an image as it is including alpha channel=-1, cv2.IMREAD_UNCHANGED
image=cv2.imread(filename=r'md.jpg', flags=-1)
cv2.imshow('my pic',image)
print(image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()