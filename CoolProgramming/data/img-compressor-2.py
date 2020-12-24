# Mass image compressing tool

# Importing the required modules
from PIL import Image
from os import path, listdir, mkdir

def main():
	""" The main function for the script """

	folderLocation = input('Enter the folder location : ')
	if path.isdir(folderLocation):
		# If the folder exists

		files = listdir(folderLocation)
		for i, j in enumerate(files):
			if j[-4:] == '.jpg' or j[-4:] == '.png':
				# If the file has extension of jpg or png, then keep
				pass
			else:
				# If the file does not has extension for jpg or png, then pop out
				files.remove(j)

		# Now proceeding with the compression
		try:
			# Using try..except.. block for the error free execution of the script
			# Asking the user for the compression level
			compression_level = int(input('Enter the compression level : '))
			# Asking the user for the output folder location
			outputFolderLocation = input('Enter the output folder location : ')
			if path.isdir(outputFolderLocation) == False:
				# If the output folder does not exists, then we create it
				mkdir(outputFolderLocation)

			if outputFolderLocation[-1] != '/':
				# Making the last character of the output folder route as '/' only if it is not already
				outputFolderLocation += '/'

			for i in files:
				if folderLocation[-1] != '/':
					# Making the folder route like "Documents/folder/" only if the user entered the folder route as "Documents/folder"
					folderLocation += '/'
				fileLocation = folderLocation + i
				outputFileLocation = outputFolderLocation + i
				img = Image.open(fileLocation)
				# Creating a new resolution for our image in a tuple format
				new_resolution = (int(img.size[0]/compression_level), int(img.size[1]/compression_level))

				# Creating an output image out of the older image
				compressed_img = img.resize(new_resolution, Image.ANTIALIAS)
				# Saving the compressed output image file to the folder with the same name
				compressed_img.save(outputFileLocation, optimize = True, quality = 90)
				print('Image resized : {}'.format(fileLocation))

			# After finishing all the compression
			print('{} files compressed and saved at {}'.format(len(files), outputFolderLocation))

		except Exception as e:
			print(e)
			quit()
	else:
		print('No such folder found : {}'.format(folderLocation))
main()
