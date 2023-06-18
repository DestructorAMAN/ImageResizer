import cv2  # openCV module

source = "Photo from Sunita Sharma.jpg"
destination = "new_resized_image.png"
scale_percent = 50  # percent by which the image is reduced

img = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("Image", img)

# calculate the 50 percent of original dimensions
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)
output = cv2.resize(img, dsize)

cv2.imwrite(destination, output)
cv2.waitKey(0)
