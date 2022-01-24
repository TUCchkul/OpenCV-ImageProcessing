import cv2
image=cv2.imread(r'md.jpg', flags=1)
point1=(150,250)
point2=(300,400)
color=(250,255,255)
thickness=25
#Draw a line
image_with_line=cv2.line(img=image,pt1=point1,pt2=point2, thickness=thickness,color=color)
cv2.imshow('Image', image_with_line)
cv2.waitKey(0)
cv2.destroyAllWindows()