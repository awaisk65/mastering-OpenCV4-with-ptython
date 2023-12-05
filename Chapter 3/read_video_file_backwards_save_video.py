#! usr/bin/env python3

# Import the required packages
import cv2
import argparse
from datetime import datetime

"""
USAGE: python3 read_video_file_backwards_save_video.py <input video path> 
"""

# We first create the ArgumentParser object
# The created object 'parser' will have the necessary information
# to parse the command-line arguments into data types.
parser = argparse.ArgumentParser()
# We add 'index_camera' argument using add_argument() including a help.
# parser.add_argument("index_camera", help="index of the camera to read from", type=int)
# We add 'video_path' argument using add_argument() including a help.
parser.add_argument("video_path", help="path to the video file")
# parser.add_argument("output_video_path", help="path to the video file to write")
args = parser.parse_args()
# We create a VideoCapture object to read from the camera (pass 0):
# capture = cv2.VideoCapture(args.index_camera)
capture = cv2.VideoCapture(args.video_path)
# Get some properties of VideoCapture (frame width, frame height and frames per second (fps)):
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print(frame_index)
fps = capture.get(cv2.CAP_PROP_FPS)
# Print these values:
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(frame_height))
print("CAP_PROP_FPS : '{}'".format(fps))

# Check if camera opened successfully
if capture.isOpened()is False:
	print("Error opening the camera")

# FourCC is a 4-byte code used to specify the video codec and it is platform dependent!
# In this case, define the codec XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Create VideoWriter object. We use the same properties as the input camera.
# Last argument is False to write the video in grayscale. True otherwise (write the video in color)
# path = "test1.avi"
path = "{}_backward_playback.avi".format(datetime.now())
out_gray = cv2.VideoWriter(path, fourcc, int(fps), (int(frame_width), int(frame_height)), False)  
# out_gray = cv2.VideoWriter(args.output_video_path, fourcc, int(fps), (int(frame_width), int(frame_height)), False)

# Read until video is completed
# frame_index = 0
while True: #capture.isOpened():
	capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
	# Capture frame-by-frame from the camera
	ret, frame = capture.read()
	if ret is True:
		# Display the captured frame:
		cv2.imshow('Input frame from the camera', frame)
		# Convert the frame captured from the camera to grayscale:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Write the grayscale frame to the video
		out_gray.write(gray_frame)
		frame_index -= 1
		# Press q on keyboard to exit the program
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break
		# Press c on keyboard to save current frame
		if cv2.waitKey(20) & 0xFF == ord('c'):
			frame_name = "camera_frame_{}.png".format(frame_index)
			cv2.imwrite(frame_name, frame)
			frame_index -= 1
	else:
		break
# Release everything:
capture.release()
out_gray.release()
cv2.destroyAllWindows()