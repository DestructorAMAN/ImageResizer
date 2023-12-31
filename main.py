import cv2  # openCV module

source = "xyz.jpg"                    #enter your image address that you want to resize.
destination = "new_resized_xyz.png"   #enter the name you want your resized image to be stored as.
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
