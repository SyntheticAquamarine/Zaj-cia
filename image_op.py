import cv2
import imutils
from Human_Detection import Detector

img = cv2.imread('C:/Users/janja/Desktop/Projekt/Pedestrian/new/walking.jpg')
img = imutils.resize(img, width=700)
img = Detector(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
