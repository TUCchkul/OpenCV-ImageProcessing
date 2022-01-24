import cv2
image=cv2.imread(r'md.jpg',flags=1)
print(image[0:100,0:100])
#Changes pixel value in the original images
#image[0:100,0:100]=255#fully white
image[0:100,0:100]=[165,42,42]#RGB format
cv2.imshow('New Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()