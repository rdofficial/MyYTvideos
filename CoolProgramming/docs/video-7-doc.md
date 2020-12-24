# Getting IP Address of a Web Server using Python

This is the extended description (documentation) for the youtube video with the same title. If you haven't watched the video yet, then [click here](https://www.youtube.com/watch?v=sjDP2vCYYmQ). The video is a part of a playlist "Cool Programmming", you can access the playlist by [clicking here](https://www.youtube.com/playlist?list=PLF0q9F-Pswkz1TrAhClq68w-4OLT3W4hQ). Below begins the main contents.

# Introduction

First of all let me say what we are going to do, We will be fetching the IP address of a web server (computer whose ports are serving a HTTP reverse proxy). Our script will work the same way as the __ping__ command of linux and windows operating systems work. We can pass the URL of the website and the IP address of the response returning web server will be returned to us. People might get confused from the term _IP address_, let me tell give you a small definition of it, _ An IP Address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. An IP address serves two main functions: host or network interface identification and location addressing_.

# Writing Code

Let's open up an text/code editor and start writing the python code. First we will begin with importing some required function from some modules in python standard library. We will import the function _gethostbyname_ from the _socket_ module. Then, we can call this function in our script with the URL of the website as the only argument. The function then returns the IP address to us, so we need to save the output of the function to a variable. Then we can do whatever we want from the fetched IP address. Let me write a small script for just printing out the IP address on the console screen (terminal screen) :
```
from socket import gethostbyname

address = input('Enter the domain address : ')
try:
	ip = gethostbyname(address)
except Exception as e:
	print('[ Error : {} ]'.format(e))
else:
	print('The IP address is {}'.format(ip))
```
Let me break down the complete source code to you. On the very first line, we import the required functions as I explained earlier. Then, we proceed to ask the user to enter the domain address of the website / webserver. Then, we get into a try..except..else block where we call the function 'gethostbyname' and save the returned IP address to a variable. If the process executes without any errors, then we print the IP address onto the console screen, or else in case of error, we print the reason of error also on the console screen. [Click here](../data/getIp.py) to view the complete source code of the script that we learnt to make today. 

# Conclusion

So, this was the tutorial. At last, we can now get a simple web server's IP address using python3. Below are some more links to interesting videos on my youtube channel related to programming : 

* Clearing python cache using shell script - [click here](https://www.youtube.com/watch?v=MB86rR9uzNo&t=16s)
* Cracking passwords using python - [click here](https://www.youtube.com/watch?v=316uQ6WyCTE&t=3s)
* Chat Bomber using just 20 lines of python code - [click here](https://www.youtube.com/watch?v=_DlxNy3KsDo)
