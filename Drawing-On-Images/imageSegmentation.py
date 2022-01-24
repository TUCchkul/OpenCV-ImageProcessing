import cv2
image=cv2.imread(filename=r'md.jpg', flags=1)
print(image[-1])
#new_image=cv2.resize(src=image,dsize=(0,0),fx=0.2,fy=0.1)
#cv2.imshow("New_Image", new_image)
#print(new_image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
