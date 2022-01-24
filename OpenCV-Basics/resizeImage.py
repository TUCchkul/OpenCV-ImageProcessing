import cv2
image=cv2.imread(filename=r'md.jpg', flags=1)
print(image.shape)
width=300
height=500
dimension=(width, height)
new_image=cv2.resize(src=image,dsize=dimension)
cv2.imshow("New_Image", new_image)
print(new_image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
