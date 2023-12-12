#pip install opencv-python

import cv2

# Read the images
large_image = cv2.imread('big.jpg')
template = cv2.imread('small.jpg')
w, h = template.shape[:-1]

# Template matching
res = cv2.matchTemplate(large_image, template, cv2.TM_CCOEFF_NORMED)

# Threshold (you may need to adjust this)
threshold = 0.8
loc = np.where(res >= threshold)

# Draw a rectangle around the match
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# Save or display the result
cv2.imwrite('result.jpg', large_image)
# cv2.imshow('result', large_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
