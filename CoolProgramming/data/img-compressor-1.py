# Importing the required modules
from PIL import Image
import os

def main():
	img_file = input('Enter the image file : ')
	if os.path.isfile(img_file) == False:
		print('No such file exists')
		quit()

	try:
		img = Image.open(img_file)
		compression_level = int(input('Enter the compression level : '))
		new_resolution = (int(img.size[0]/compression_level), int(img.size[1]/compression_level))
		compressed_img = img.resize(new_resolution, Image.ANTIALIAS)
		output_img = input('Enter the ouput image file name : ')
		compressed_img.save(output_img, optimize = True, quality = 90)
	except Exception as e:
		print(e)
		quit()

main()
