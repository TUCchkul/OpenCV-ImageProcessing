import cv2
image=cv2.imread(r'md.jpg', flags=1)
start_point=(50,50)
end_point=(400,200)
thickness=5
color=(0,0,255)
new_image=cv2.rectangle(image, pt1=start_point,pt2=end_point, color=color, thickness=thickness)
cv2.imwrite('D:\OPENCV-ImageProcessing\OpenCV-ImageProcessing\Drawing-On-Images\bici-muhammad.jpg', new_image)
cv2.imshow('image', new_image)
cv2.waitKey()
cv2.destroyAllWindows()