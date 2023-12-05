#! usr/bin/env python3

# Import the required packages
import cv2
import numpy as np

# Dictionary containing some colors
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255),
'yellow': (0, 255, 255), 'magenta': (255, 0, 255), 'cyan': (255, 255, 0),
'white': (255, 255, 255), 'black': (0, 0, 0), 'gray': (125, 125, 125),
'rand': np.random.randint(0, high=256, size=(3,)).tolist(), 'dark_gray':
(50, 50, 50), 'light_gray': (220, 220, 220)}

global left_mouse_x, left_mouse_y, right_mouse_x, right_mouse_y

def draw_circle(event, x, y, flags, param):
	global left_mouse_x, left_mouse_y, right_mouse_x, right_mouse_y
	if event == cv2.EVENT_LBUTTONDBLCLK:
		cv2.circle(image, (x, y), 10, colors['magenta'], -1)

	if event == cv2.EVENT_LBUTTONUP:
		# cv2.line(image, (window_x, window_y), (x, y), colors['green'], 3)
		cv2.rectangle(image, (left_mouse_x, left_mouse_y), (x, y), colors['blue'], 2)

	if event == cv2.EVENT_LBUTTONDOWN:
		left_mouse_x = x
		left_mouse_y = y

	if event == cv2.EVENT_RBUTTONUP:
		cv2.line(image, (right_mouse_x, right_mouse_y), (x, y), colors['green'], 3)

	if event == cv2.EVENT_RBUTTONDOWN:
		right_mouse_x = x
		right_mouse_y = y

image 	 = np.zeros((650, 650, 3), dtype="uint8")
image[:] = colors['white']

cv2.namedWindow('Image mouse')

cv2.setMouseCallback('Image mouse', draw_circle)

cv2.putText(image, "Double left click: add circle on current mouse pose", (10, 600), 1, 1, colors['black'], 1, cv2.LINE_AA)
cv2.putText(image, "Simple left click and drag: add rectangle", (10, 615), 1, 1, colors['black'], 1, cv2.LINE_AA)
cv2.putText(image, "Simple right click and drag: add line", (10, 630), 1, 1, colors['black'], 1, cv2.LINE_AA)
cv2.putText(image, "Press 'q' to exit", (10, 645), 1, 1, colors['black'], 1, cv2.LINE_AA)


while True:
	cv2.imshow("Image mouse", image)
	if cv2.waitKey(20) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()