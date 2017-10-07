# -*- coding:UTF-8 -*-
import numpy as np
import argparse
import imutils
import glob
import cv2

def auto_canny(image, sigma = 0.33):
	v = np.median(image)
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	return edged

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True)
args = vars(ap.parse_args())

for imageParth in glob.glob(args["image"] + "\\*.jpg"):
	image = cv2.imread(imageParth)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray, (3, 3), 0)

	wide = cv2.Canny(blur, 10, 200)
	tight = cv2.Canny(blur, 225, 250)
	auto = auto_canny(blur)

	cv2.imshow("wide", imutils.resize(wide, width = 400))
	cv2.imshow("tight", imutils.resize(tight, width = 400))
	cv2.imshow("auto", imutils.resize(auto, width = 400))
	cv2.waitKey(0)