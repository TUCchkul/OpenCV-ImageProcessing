import cv2
images=cv2.imread(r'md.jpg', flags=1)
center=(300,300)
RADIOUS=100
color=(254,2,255)
thickness=5
circle_md=cv2.circle(img=images, center=center, radius=RADIOUS, color=color, thickness=thickness)
cv2.imshow('image', circle_md)
cv2.imwrite("D:\OPENCV-ImageProcessing\OpenCV-ImageProcessing\Drawing-On-Images\bichi-muhammad.png",circle_md)
cv2.waitKey()
cv2.destroyAllWindows()