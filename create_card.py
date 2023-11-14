import cv2
img = cv2.imread("poster.jpg")
rocket = img[120:300, 400:500]
img[0:240, 500:600] = rocket
text_to_show = "eu adoro progamar"
cv2.putText(img, text_to_show, (20, 220),fontFace= cv2.FONT_HERSHEY,fontScale=0.6, 
color=(0, 191, 255))
cv2.imshow("resultado", img)
cv2.waitKey(0)

import cv2

img = cv2.imread("poster.jpg")


rocket = img[120:300, 400:500]


img[0:240, 500:600] = rocket


text_to_show = "Eu adoro programar"


cv2.putText(img, text_to_show, (20, 220), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.6, color=(0, 191, 255), thickness=2)


cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()