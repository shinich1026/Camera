import cv2
import os

#read
image_path = os.path.join('.', 'data', 'Cat.jpg')
img = cv2.imread(image_path)

#write
cv2.imwrite(os.path.join('.', 'data', 'Cat.jpg'), img)