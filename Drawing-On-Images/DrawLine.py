import cv2
image=cv2.imread(r'md.jpg', flags=1)
point1=(150,250)
point2=(300,400)
color=(250,2,255)
thickness=25
#Draw a line
#image_with_line=cv2.line(img=image,pt1=point1,pt2=point2, thickness=thickness,color=color)
#Draw arrow
image_with_line=cv2.arrowedLine(img=image,pt1=point1,pt2=point2, thickness=thickness,color=color, tipLength=1.2)
cv2.imshow('Image', image_with_line)
cv2.imwrite('D:\OPENCV-ImageProcessing\OpenCV-ImageProcessing\Drawing-On-Images\Propfet-Muhammad.jpg',image_with_line)
cv2.waitKey(0)
cv2.destroyAllWindows()