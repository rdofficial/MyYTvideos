# Image Compressing Tool in Python #2

This is the extended documentation for my youtube video of the playlist ["Cool Programming"](https://www.youtube.com/watch?v=KQJ_WwxJJ7c), if you haven't watched the video yet, then [click here](https://youtube.com/). So now the documentation begins, enjoy the boring :-) reference.

The video is the second part of the previous [video](), if you haven't watched the video yet then, below are required links for the previous video and related data :
* 1st part of video on youtube : [click here](https://www.youtube.com/watch?v=ySTIatu5Alg).
* Source code for 1st part : [click here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/data/img-compressor-1.py)
* Documentation for 1st part : [click here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/docs/video-1-doc.md)

In this tutorial, we are going to add a little advancement to our __Image compressing tool__, and that is we are going to make it a __Mass image compressing tool__. So we will follow the same algorithm for compressing each image of an folder. If you don't know the algorithm through which we are going to compress the image, then [click here](https://github.com/rdofficial/MyYTvideos/blob/master/CoolProgramming/docs/video-1-doc.md) to checkout the documentation for that. In the script, we are going to use the __Pillow (PIL)__ and the __os__ module. We are specifically going to use the __Image__ class from the PIL module, and the listdir, path and mkdir.

Let me explain these functions of the OS module in brief :
* __listdir__ :- The function returns the list of files and folders inside the directory mentioned in the parameter, and if no directory location in the parameter then it returns the contents of the currently active folder. Syntax :
```
from os import listdir
filesList1 = listdir()		# Returns the content for the current directory
filesList2 = listdir('/home/user/Documents')		# Returns the content for the directory "/home/user/Documents"
```

* __mkdir__ :- The function from the OS module to create a folder, the parameter required by the function is the path of folder that needs to created. For example :
```
from os import mkdir
mkdir('/home/user/testfolder')
```
There are errors that may arise in some case, like if the folder already exists then, error arises. We will use the function to create the output directory if it does not exists.

* __path__ :- The separate sub library which comes under the os module includes functions for working and manipulating the files and directory locations. Like the function __path.isfile()__ is to check wheter a file exists or not, and the __path.isdir()__ is a function for verfication wheter a directory exists or not. We will use the functions path.isdir() in our script.

## Writing the code

I am using the nano code editor in this tutorial, but you can use any other code editors whatever you like. The source code of the script is available, also the source code includes easy language comments to expertise better understanding of yours. The writing of the code with explanation is defined properly with separate sections for each section of the code (e.g., importing of the modules, defining functions, taking user input and validation, etc).

* __Importing modules__ :- 
A python script is incomplete without a external library, thats why we are doing so, just kidding, the script requires some libraries to be imported in order to work properly. Firstly we are going to import the required functions and classes. We will import the Image class from PIL module through which we are going to write the image file with newer resolution in order to reduce its size, also we are importing listdir(), path library, and mkdir() of the os module for listing files and folder, working with directories and validation of the directories. Here we write the import block of the script.
```
from PIL import Image
from os import path, listdir, mkdir
```

* __Writing the main function__ :- 
I am kinda old C fashioned person, thats why I always write a main function and later call it in the script, so as we know in python we use the _def_ keyword to define a custom function which will enclose our entire programs source code. I do this method below
```
def main():
	""" This is the doc string for the main function, write whatever the hell you want """

	# Statements

main() # Do not forget to call the main function
```

Do not forget to call the main function, otherwise after writing the whole source code, when the program does not works, you'll keep wondering that why in the world is your script not running. I usually call the main function using below type code blocks, if you get confused with the below way of calling then use the simple way
_Simple statement to call the main() function_
```
main()
```
_or_
_My way to call the main() statement_
```
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# Exiting the program when the user presses CTRL+C
		exit()
```

* __Getting the inputs from the user__ :-
We will ask the user for directory location from which the image files are about to be picked up, also we will ask for the compression level and the output directory location where the result / output images are to be saved. We will enclose all the code in the main() function.
```
def main():
	""" The main function """

	folderLocation = input('Enter the directory location : ')
	compression_level = int(input('Enter compression level : '))
```

We also need to verify wheter the directory entered by the user exists or not, for that purpose we will use the the path.isdir() function. ( For basic knowledge, path.isdir() function takes the location of the folder as paramter and return a boolen type ). Here we write the code and insert it in the main() function.
```
if path.isdir(folderLocation) == False:
	# If the specified folder does not exists, then we return an error and quit the script

	print('Error : No such folder exists')
	exit()
```
Now we will get the list of the files in the user specified directory. For getting the list of files, we will use the listdir() function from os module. We will use the below piece of code to iterate through each file in the requested directory, and the below code should be inserted into the main function
```
for fileName in listdir(folderLocation):
	# Iterating through each of the image file names
	fileLocation = path.join(folderLocation, fileName) # Joining the folder location to the complete path for no errors
```

Before starting the compression process we will ask the user for the output directory and verify it in the same way the folderLocation directory was verified, if the directory exists, then we continue, if the directory does not exists, then we create it.
```
outputFolderLocation = input('Enter the output folder location : ')
if path.isdir(outputFolderLocation):
	pass
else:
	mkdir(outputFolderLocation)
```

* __Verifying the image files in the folder :-__
Now we will verify the image files in the user specified folder, that wheter they are really image files or not. If they are not image files, then we will skip the process of the compression on them to avoid the errors. Here is the code for doing so, and insert the code inside the for loop.
```
if fileName[-4:].lower() == '.jpg' or fileName[-4:].lower() == '.png' or fileName[-4:].lower() == 'jpeg':
	# If the file is really an image file, then we proceed into the compression

	# Statements for compression
else:
	# If the file is not an image file, then we skip the process of the compression on it. We will use the continue statement for skiping the file in the loop

	continue  
```

* __Compression of each image in the folder__ :-
Now we will proceed to the compression process of the each image file. We will insert the below specified code in the for loop. First we will open the current image file in the Image object and work out with its resolution (size). Then we are going to make a new resolution in the tuple data type. We will use the existing resolution of the image and reduce it by dividing it by the compression level specified by the user. Note that the items in the resolution tuple should be of the int data type. We will then create a new image object forked from the older image but with newer resolution as calculated by the script. Then we create a saving path for the compressed output image and save it. The whole process uses the below codes.
```
img = Image.open(fileLocation)
new_resolution = (int(img.size[0]/2), int(img.size[1]/2))  # Creating the new resolution
compressed_img = img.resize(new_resolution, Image.ANITIALIAS)

# Creating a path for saving the image
outputFileLocation = path.join(outputFolderLocation, fileName)

# Saving the requested image file to the output folder with the same original name
compressed_img.save(outputFileLocation, optimize = True, quality = 90)
```

* __Handling the errors :-__
The main part of the programming is to find bugs and fix them, If not fix them then atleast try to minimalize their impact on the user experience.
