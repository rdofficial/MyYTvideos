# Clear Screen in C Program

This is the extended description / documentation for my youtube video of the same name, if you have not watched the video yet then [click here](). The video is a part of the playlist __Cool Programming__, if you have not accessed the playlist yet, then [click here](). The documentation starts below :

Today we are going to learn to make a console screen clearing feature in a C program. Often writing a C program, we must feel like that the console screen gets filled constantly with other elements like older outputs, etc. For that clearing purpose, we use the system's command for clearing the terminal screen i.e., clear in linux and cls in windows. This creates a difference between the codes that we need to type, often we have to endup using system dependent libraries like __windows.h__ for windows code and __unistd.h__ for linux based code. This makes the program confusing and at the same time is memory consuming. But we have brought a new initiative for printing a new technique that works for both linux and windows, but honestly there isn't. 

So now basically, I said there are no perfect techniques for clearing screen in C, because C is a low level language designed to handle hardware close programs and functionalities, also C does not understands the concept of the screen, only way to do so is to write a bunch of header files for clearing the screen also after defining the screen adaptibility. But for Unix and linux based systems, we can use a simple _regex_ __\e[1;1H\e[2J__. This code might not work for the windows systems, but we can use the clrscr() function from the header conio.h header file ( We will discuss that later ).

## Writing the C Program

Basically the regex _\e[1;1H\e[2J_ prints the cursor back to the same point after skipping some lines. We can use this technique to clear the screen. We will simply use a loop to print the regex using atleast 500 times. We will define a simple function for the purpose, later we can import this function in our program either by just typing it in the source code, or else we can define it in a header file and then include it. Below is the function defined for clearing the screen using the regex.
```
#include <stdio.h>

void clearScreen() {
	/*
The function for clearing the screen.
The function requires the stdio.h header to be included in the program as it uses the printf function

	for (int i = 0; i < 500; i++) {
		printf("\e[1;1H\e[2J");
	}
}
```
Thus we can use the above clearScreen() function whenever we feel to clear the console screen in our program. I have written the function in an example C program, [click here](../data/clear-screen.c) to access the source code.


If you have any doubts regarding the tutorial, you can contact me at my [instagram handle](https://instagram.com/rdofficial192).
Below are some links that can be helpful to you :
* Image compressing tool in python : [click here](https://www.youtube.com/watch?v=ySTIatu5Alg)
* Shell script to clean python cache : [click here](https://www.youtube.com/watch?v=MB86rR9uzNo)
* Cracking passwords using python : [click here](https://www.youtube.com/watch?v=316uQ6WyCTE)
