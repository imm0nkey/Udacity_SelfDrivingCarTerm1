# Do relevant imports
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

cv2.destroyAllWindows()
# Read in and grayscale the image
# image = mpimg.imread('solidWhiteCurve.jpg')
# image = mpimg.imread('solidWhiteRight.jpg')
# image = mpimg.imread('solidYellowCurve.jpg')
# image = mpimg.imread('solidYellowCurve2.jpg')
# image = mpimg.imread('solidYellowLeft.jpg')
# image = mpimg.imread('whiteCarLaneSwitch.jpg')
videoCapture = cv2.VideoCapture("solidWhiteRight.mp4")
videoCapture.set(cv2.CAP_PROP_POS_FRAMES, 162)
ret, image = videoCapture.read()
# image = mpimg.imread("solidWhiteRight/161.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
plt.imshow(edges)
plt.show()

# Next we'll create a masked edges image using cv2.fillPoly()
mask = np.zeros_like(edges)
ignore_mask_color = 255

# This time we are defining a four sided polygon to mask
imshape = image.shape
vertices = np.array([[(0, imshape[0]), (480, 320), (490, 320), (imshape[1], imshape[0])]], dtype=np.int32)
cv2.fillPoly(mask, vertices, ignore_mask_color)
plt.imshow(mask)
plt.show()
masked_edges = cv2.bitwise_and(edges, mask)

# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 2
theta = np.pi/180
threshold = 15
min_line_length = 40
max_line_gap = 20
line_image = np.copy(image)*0  # creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)

# Iterate over the output "lines" and draw lines on the black
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges))
mask_3 = np.dstack((mask, mask, mask))

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
# plt.imshow(combo)
# plt.show()
combo = cv2.addWeighted(image, 0.8, line_image, 1, 0)
plt.imshow(combo)
plt.show()

combo_image_mask = cv2.addWeighted(image, 0.8, mask_3, 0.2, 0)
# plt.imshow(combo_image_mask)
# plt.show()
