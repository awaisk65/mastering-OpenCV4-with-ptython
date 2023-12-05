#!/usr/bin/env python3

import argparse
import cv2

"""
USAGE: python3 argparse_load_image.py <path to image>
"""

parser = argparse.ArgumentParser()

parser.add_argument("image_path", help="Path of input image")

args = parser.parse_args()

image = cv2.imread(args.image_path)

args = vars(parser.parse_args())

image2 = cv2.imread(args["image_path"])

cv2.imshow("Image 1 ", image)
cv2.imshow("Image 2 ", image2)


cv2.waitKey(0)
cv2.destroyAllWindows()