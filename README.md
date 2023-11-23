SIFT Matching for Pixel Phone Box Images
Overview
This project involves utilizing the SIFT (Scale-Invariant Feature Transform) algorithm to perform feature matching between images of Pixel phone boxes. The goal is to identify and match distinctive keypoints in the images, demonstrating the robustness of SIFT in recognizing objects across different orientations.

Images Used
Reference Image (pix7a.jpeg):

This is the reference image of a Pixel phone box.
Rotated Image (pix7a_rot.jpeg):

This image is a rotated version of the reference image, simulating a change in orientation.
Procedure
Image Loading:

The project starts by loading two images of Pixel phone boxes.
SIFT Algorithm:

The SIFT algorithm is applied to detect and describe keypoints in both images.
Feature Matching:

A brute-force matcher is used to find matches between the keypoints of the reference and rotated images.
Visualization:

The matches are visualized using the cv2.drawMatches function to illustrate the effectiveness of SIFT in matching features despite changes in orientation.
How to Replicate
To replicate this project:

Ensure you have the required libraries installed (cv2, matplotlib).
Clone this repository.
Replace the sample images (pix7a.jpeg and pix7a_rot.jpeg) with your own images if needed.
Run the provided Python script or Jupyter Notebook to observe the SIFT feature matching results.
Results
The output image (img3) will showcase the matched keypoints between the reference and rotated images, demonstrating the ability of SIFT to handle changes in orientation.

Feel free to experiment with other images or use this project as a template for SIFT feature matching in different scenarios.
