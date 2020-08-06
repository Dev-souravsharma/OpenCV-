import cv2
import numpy as np

img = np.zeros([512, 512, 3], np.uint8)
cv2.line(img, (7, 73), (255, 255), (255, 0, 0), 5)
cv2.arrowedLine(img, (177, 73), (255, 255), (255, 0, 0), 5)
cv2.rectangle(img, (7, 73), (255, 255), (255, 0, 0), 5)
cv2.circle(img, (7, 73), 50, (255, 0, 0), 5)
cv2.putText(img, 'Sourav', (10, 500), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
