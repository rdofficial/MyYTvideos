# Shell Script to clean python cache

This is the extended documentation for my youtube video, if you haven't watched the video yet, then [click here](https://www.youtube.com/watch?v=MB86rR9uzNo) to watch the video. The video shows to write a shell script for clean python cache in the linux filesystem. The video is a part of a playlist [Cool Programming](https://www.youtube.com/playlist?list=PLF0q9F-Pswkz1TrAhClq68w-4OLT3W4hQ), if you have not accessed the playlist yet, then go on and then watch more such interesting contents. Below starts the main documentation or you can call it extended description.

Generally when we run any python scripts, there are cache files formed with extension __.pyc__. These are generally compiled object code for the scripts and modules we use in the python programs. When we run the python program, the python interpreter converts the high level source code to an machine level object file, that can be run by the computer system. These files takes up a lot of space on the hard disk when stored over a long time. Thus to clean up some space, lets write some code. But before writing some codes let us learn some important commands.

### Finding the __pycache__ folders
The *__pycache__* folders are stored diversely on the linux filesystem, so in order to find them we need to use the __find__ command on the linux terminal with some filters. Generally the find command prints the complete locations for the files and folders inside a specific directory. As a filter we will use a pipe (|) with grep command, and the grep command will be fetching all the file locations containing the term *__pycache__*. So we will use the below command.
```
find / | grep __pycache__
```

We will use the find command in the main root filesystem (/) for searching all over the system. So for error free execution make sure you have sudo (root) previleges on the linux system you are working on. For entering the root terminal we can either log in with root account or just simply type the command _sudo bash_ in the terminal and then enter the root terminal.
Then post the result of the find command is a long bunch of files and folders locations. We can do nothing with them, unless deleting them one by one. Instead we will write a basic bash (shell) script with some looping instructions and conditional statements.

### Writing the script

* __Variables :-__ Variables are a important part of a program / script. We will use a simple variable here for containing the output of the find command. In bash scripting, the variable can be assigned like :
```
name="Happy Programmer"
```
But when it comes to use a variable in any command or function, we need to add an $ prefix to it for getting the value to it. Like this way.
```
echo $name
```
But when we want to assign the ouput of a command to a variable, we will use the code like
```
result=$( apt update )
```
Here we are going to write the output of the find command to the variable and name it 'list'. We will use the below block of code.
```
# Assigning all the pycache folders and the files to a variable named list
list=$( find / | grep __pycache__ )
```

* __Using for loop to iterate :-__ Now we will iterate through the list variable using for loop to delete each of the files and folders. The syntax for iterating through a such variable is given below :
```
for i in $string
do
	# Code to work with string variable's iterated value
done
```
For our script we will use the below piece of code :
```
for i in $list
do
	# Code to delete the file / folder location stored in variable i
done
```

* __Deleting only folders :-__ We will delete only the folders, because deleting the folders will also delete the file inside them and also reduce the conflicts of errors. We will use a conditional if statement for identifying wheter a folder or not. As we know the if statement to check wheter the location provided is really a folder or not is
```
if [[ -d "/location/to/folder" ]]; then
	# Code to do something
fi
```
In our script we will use this code inside the for loop to check wheter the location in the value of i is a folder or not. If it is a folder, then we use the __rm__ command to delete the folder. Also do not forget to use the rm command with a _-r_ flag. The code for that is below :
```
for i in $list
do
	if [[ -d $i ]]; then
		# If the specified location is a folder, then only we delete it

		rm -r $i
	fi
done
```

* __Printing progressions to the console :-__ During the execution of the script, we need to know that wheter the script is working or not. Sometimes the script may get struck in some moments that we cannot identify that wheter it is a error or just a slow process. We will use the echo command to inform the progress of the script, like we will put a echo message command after scanning the folders and also after execution of the script.

### Final code
The final script looks something like the below one, although you can modify the script as per your choice.
```
# Scanning for the folders
echo "Scanning for python cache folders"
list=$( find / | grep __pycache__ )

echo "Deleting the python cache folders"
for i in $list
do
	if [[ -d $i ]]; then
		# If the location is of a folder, then we delete it

		rm -r $i;
	fi
done

echo "All the python cache folders are deleted"
```


### Conclusion
Thus the script is completed for cleaning python cache. In the same way, we can clean the other application's cache data like for apt, npm, ruby, etc. At the end of the doc, hope you have understood the explanation for the code. To read the original source code, [click here](https://github.com/rdofficial/MyYtVideos/blob/main/CoolProgramming/data/pycleaner).
For any further information, contact me at my [instagram handle](https://instagram.com/rdofficial192).
