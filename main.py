import cv2
import matplotlib.pyplot as plt

# read images
img1 = cv2.imread('pix7a.jpeg')
img2 = cv2.imread('pix7a_rot.jpeg')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# SIFT (check OpenCV version to handle the change)
if cv2.__version__.startswith('3'):
    sift = cv2.xfeatures2d.SIFT_create()
elif cv2.__version__.startswith('4'):
    sift = cv2.SIFT_create()
else:
    raise ImportError("Unsupported OpenCV version")

keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)

# feature matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1, descriptors_2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
plt.imshow(img3)
plt.show()
