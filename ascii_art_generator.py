import cv2
import sys
import numpy as np

def pixel_to_ascii(img):
	ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
	output = []
	for i in range(img.shape[0]):
		temp = ''
		for j in range(img.shape[1]):
			temp += ASCII_CHARS[img[i][j]//25]
		output.append([temp])
	return output

def main():
	path = sys.argv[1]
	# print('image path: ', path)
	img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

	ratio = 100/img.shape[1]
	img = cv2.resize(img, None, fx = ratio, fy = ratio)
	# print(img.shape)

	ascii_art = pixel_to_ascii(img)
	for s in ascii_art:
		print(s[0])

	output = 'ascii_' + path.split('/')[-1].split('.')[-2] + '.txt'
	with open(output, 'w') as f:
		for s in ascii_art:
			f.write(s[0]+'\n')



main()