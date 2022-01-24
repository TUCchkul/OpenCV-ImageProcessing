import cv2
image=cv2.imread(r'md.jpg', flags=1)
CENTER=(100,100)
AXES=(50,50)
ANGLE=0
START_ANGLE=0
END_ANGLE=360
THICKNESS=3
COLOR=(0,255,0)
new_image=cv2.ellipse(img=image, center=CENTER,thickness=THICKNESS,angle=ANGLE, startAngle=START_ANGLE,endAngle=END_ANGLE,axes=AXES,color=COLOR)
cv2.imshow('image', new_image)
cv2.imwrite('D:\OPENCV-ImageProcessing\OpenCV-ImageProcessing\Drawing-On-Images\bici-Muhammad.jpg',new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()