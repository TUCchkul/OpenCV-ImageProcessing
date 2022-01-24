import cv2
image=cv2.imread(filename=r'md.jpg', flags=1)
print(image.shape)
width=300
height=500
dimension=(width, height)
#new_image=cv2.resize(src=image,dsize=dimension)
#fx=width,fy=height
new_image=cv2.resize(src=image,dsize=(0,0),fx=0.1,fy=0.1)
cv2.imwrite(r'D:\OPENCV-ImageProcessing\OpenCV-ImageProcessing\OpenCV-Basics\new_imag.png', new_image)
cv2.imshow("New_Image", new_image)
print(new_image.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
