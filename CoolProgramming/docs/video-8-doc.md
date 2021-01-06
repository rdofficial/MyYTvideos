# Chat Bomber using Python

This is the documentation (extended description) for the [video]() at [my youtube channel]() wih the same title. If you haven't watched the video yet, then [click here]() to watch it, it would make you experience a better practical version of the tutorial. So, let's continue proceeding to the documentation version tutorial.

## Introduction

Today's tutorial is about creating a chat bombing using just a few lines of python code. Before proceeding further, let me tell you what is a chat bomber. A chat bomber is a tool that is used to send a thousands of messages continously to a particular user. We will use python for this purpose, and show you that how simple is really the process of creating a chat bomber is. You can use this technique to annoy your friends by sending them a hell lot of messages. There are no any bigger explanations for the concept, just read the process below.

## Process

First we will install the required modules by our script, use the below command s for installing the __pyautogui__ and __pynput__ modules.
```
pip3 install pyautogui pynput
```
After installing the required modules, we will proceed onto writing the script. Open up a code editor and create a new file named _chat-bomber.py_ and then start writing the code.
First we will write the code for importing the required modules
```
import pyautogui,time, os, sys
from pynput import keyboard
```
Now we will write the main function for the script which will execute the major processes. Below is the code for that function.
```
# The text to be typed in the bombing process (Change it as per your choice)
text = 'Happy Bombing'

def on_press(key):
        """ """

        if str(key) == 'Key.esc':
                sys.exit()
        elif str(key) == 'Key.enter':
                pyautogui.typewrite(text)
                pyautogui.press('enter')
                time.sleep(0.25)
```
Let's break the code down into steps.
* First we are going to declare a string variable _text_ which stores the string value of the characters which are going to typed by the script in per message which is sent.
* Then, we declare a function named on_press(key) which takes a argument _key_. The argument is the keystroke pressed on the keyboard by the user. We will use this key to check that which key is pressed by the user and then manipulate the flow of the script as per the key.
* Then, we use a if..elif statements block, where we will check if the 'ESC' key is pressed then we exit the script (Stop the bombing process).
* If the key pressed by the user is 'enter' key, then we keep typing the text and pressing enter key. Here, we again order the python script to press enter key as the enter key is used to send a message in almost all the chatting services (including WhatsApp and Instagram). Also, we keep a time sleep of a quarter of a second in order to not make the computer get hanged (slow, buggy).

Now let's write the code for the listener for the keyboard.
```
try:
        with keyboard.Listener(on_press = on_press) as listener:
                listener.join()
except Exception as e:
        pass
finally:
        print('Exiting bomber')
```
The above code block will run the function as long as we do not press the 'ESC' key. So, this was the code for the entire script. Just now save the file and run it using the below command on the terminal.
```
python3 chat-bomber.py
```
Then move the mouse cursor to the message typing box for the chatting application (in web browser), and press enter key. Then, the real magic starts ;-). To stop the bomber just press ESC key.

## Conclusion

At last after completing the tutorial, hope you have grasped all the processes and concepts of the tutorial. If you still have doubts, then can kindly leave a comment on the youtube video tutorial, I will surely help you with your errors and doubts. Below are some links to more tutorials that you might like :

* Basic Encryption using Python : [Click here](video-6-doc.md)
* Getting IP Adress using Python : [Click here](video-7-doc.md)
* Image compressing tool in Python : [Click here](video-1-doc.md)
