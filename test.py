import cv2
image = cv2.imread("img_name.jpg")       #Inserting the image file
cv2.imshow("org_img", image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      #Converting the given image file into grey_scale image
cv2.imshow("gray_img", gray_image)
cv2.waitKey(0)
inverted_image = 255 - gray_image        #Inverting the obtained grey_scale image
cv2.imshow("inverted_img", inverted_image)
cv2.waitKey()
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)      #Blurring the new updated image
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)      #Finally giving it the sketch look
cv2.imshow("sketch_img", pencil_sketch)
cv2.waitKey(0)
cv2.imshow("original_image", image)
cv2.imshow("pencil_sketch", pencil_sketch)
cv2.waitKey(0)
