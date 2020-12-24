# Image compressing tool in python #1

This is the documentation of my youtube video and this can be used as a reference to what I say in that video. Below goes the doc / extended version of the documentation.

We are creating an image compressing tool in python for resizing image files (JPG/PNG). Before starting this video, you should have knowledge of basics python and famliar with its syntax as well as basic terms. We will use an external python module in this script named __Pillow__, which can be installed using the pip.
Use these commands in the terminal
```
pip3 install Pillow
```
__or__
```
python3 -m pip install Pillow
```

### Basic introduction to Pillow library
The Pillow library or the __PIL__ (Python Imaging Library) adds image processing capablities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capablities. The core image library is designed for fast access to data stored in a few basic pixel formats.

We will be using this library for compressing the image file and the rest alteration of the pixel data will be carried on by the pre written code in the library. We will be using the PIL module of the library and will be using the Image class for operating on the user specified image.

### Starting with the code
After successfull installation of the Pillow library, we will import the library using the below code (Also we will import __os__ module) :
```
from PIL import Image
import os
```

We will be asking the user for the filename and location and assign the input string value to a variable, then we will proceed with verifying wheter the file exists or not using the __os.path.isfile__ method. We will use the below block of code for this purpose.
```
img_file = input('Enter the image file : ')
if os.path.isfile(img_file) == False:
	# If the user entered file does not exists then show errors and exit the script
	# Statements to run

# Script with proceed executing further commands if the file entered by the user exists
# Statements to run
```

The above block of code can also be interpreted as :
```
img_file = input('Enter the image file : ')
if os.path.isfile(img_file):
	# If the user entered file exists on the system, then we proceed with compressing the file
	# Statements to run
else:
	# If the user entered file does not exists then show errors and exit the script
	# Statements to run
```

### Processing an image file using PIL
We will learn on how to process image files using the Image object of the PIL module. Below codes gives better illustration
```
# Opening an image file
img = Image.open(image_file_location)

# Getting the image file current resolution
resolution = img.size
```

Before writing the above commands in our script, we will ask the user for the lcoation of the image file and save it to a variable which will be passed to the Image.open method.

The image resolution is generally in tupple format, like (1440, 720). We have to reduce them by dividing with special numbers and placing there integral form. Just like below 
```
# We will take input from user for the compression level
level = int(input('Enter the compression level : '))

# Making new resolution in tuple format
new_resolution = (int(resolution[0]/size), int(resolution[1]/2))
```
Note that we have taken the compression level input from the user and that too in int format. Also we proceeded with making the new resolution in int data type.

Now we will proceed onto creating a new __Image__ object with our new resolution with the help of the method __resize()__ ( The method is from the Image class ). The syntax for the method is as below.
```
self.resize(resolution, Image.ANTIALIAS)
```
We will use the below lines of code :
```
compress_img = img.resize(new_resolution, Image.ANTIALIAS)
```

Now we will proceed to save the image in the user desired location. We will ask the user for the output location. For this purpose, we will use the below lines of code :
```
output_location = input('Enter the output location : ')
compressed_img.save(output_location, optimize = True, quality = 90)

# Here we also set two other labels / parameters, that are optimize to True and quality to 90. The label "optimize" is set to True that means the image will be compressed as much as extent as could. Also we set the quality percentage to 90% 
```


### Joining all the code

We will proceed to write the entire code into a function named __main__ except the import statements. After writing all those short code, the code will look like this :
```
from PIL import Image
import os

def main():
	img_location = input('Enter the image file : ')

	# Statements for processing the image
	img = Image.open(img_location)
	compression_level = int(input('Enter the compression level : '))
	new_resolution = (int(img.size[0]/compression_level), int(img.size[1]/compression_level))
	compressed_img = img.resize(new_resolution, Image.ANTIALIAS)
	
	# Asking the user for the location of the output compressed image file
	output_location = input('Enter the output location : ')
	compressed_img.save(output_location, optimize = True, quality = 90)
	print('Image compressed and saved at : {}'.format(output_location)

# Don't forget to call the main function otherwise our hard work will flush down the drainage :-)
main()
```

### Handling the errors

For proper execution of the script and user reliablity, the script needs to run in an error free execution. For accomplising this goal, we need to use the __try..except..__ statements for the above code. We will write the statements which deal with image processing in the _try_ block and the _except_ block with the following code :
```
try:
	# Image processing / compressing statements
except Exception as e:
	# We first stored the error raised in variable named 'e'

	print(e)
	quit()
```

What we have done in the except block is that we have saved the error statement in a variable named 'e' and then printed the error to the console screen also exit the program at that instance.

The final error free code will look like this

```
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
```

For more detailed code, watch the source file [here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/data/img-compressor-1.py).

### Wrapping up 

On the conclusion, we have created a basic image compressing tool in python, but we have learnt the algorithm for compressing image files. Now we can proceed in compressing multiple or mass files using the same script. Yes, nice guess, we are going to make the version 2 of this script i.e., mass image compressing tool in the next video of the playlist.

If you haven't watched the video yet, [click here](https://www.youtube.com/watch?v=ySTIatu5Alg&feature=youtu.be) to watch the video.
If you have any queries or doubts, then comment below the video and also can DM me at my [instagram handle](https://instagram.com/rdofficial192)

Some other links are :
* Source code file - [click here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/data/img-compressor-1.py)
* Playlist Documentation - [click here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/README.md)
* My youtube channel - [click here](https://youtube.com/channel/UCfp-xR7cpyLOXVW8MYr59WA)
* My instagram profile - [click here](https://instagram.com/rdofficial192)


__PEACE__ :-)
