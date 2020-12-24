# Simple Encryption using python

This is the extended description / documentation for my youtube video with the same name, if you have not watched the video yet then [click here](https://www.youtube.com/watch?v=hNcvdq6daJA). The video is a part of the playlist "_Cool programming_", if you have not accessed the playlist yet, then [click here](https://www.youtube.com/playlist?list=PLF0q9F-Pswkz1TrAhClq68w-4OLT3W4hQ). Below starts the documentation ( You can also call it a tutorial ).

## Introduction

Today we are going to make a simple string encryption python script. So basically what is __Encryption__? Encryption means conversion of plain text to a cipher text format that is unreadable to and meaningless. This makes our data more and more secure. As only we are the one who can revert the data back to the original format. The term encryption comes under a subject cryptography. The whole cryptography and other related terms are defined below one by one :

* __Cryptography :-__ Cryptography is a method of protecting information and communications through the use of codes, so that only those for whom the information is intended can read and process it. The prefix "crypt-" means "hidden" or "vault" -- and the suffix "-graphy" stands for "writing". Cryptography is often used in web servers for securely saving their user's private data in either the filesystem or the database. There are many types of cryptography based on what algorithms are used to hide the bytes of the data. There are password protected cryptography which can be used for the encryption of files and data as per a particular user wants to. Popular algorithms to use are LSB and Bit-wise. There are media based cryptographic methods, also called as steganography where we hide our data into media files like images, videos, and music.

* __Basic encryption :-__ The very basic encryption method is switching the characters to another characters in an algorithm / order. Like we can write a -> 102 and rest remaining characters as something predefined, this makes sure that the only one who knows the complete translation knows the actual meaning of the cipher text. Now in programming we can switch the character base numbers, like extend the char code of a character to certain jump number. Like we can switch the characters from user defined jump number, like below program output.
```
Enter the jump number : 4
Enter the text : Happy Programming
|--------------------------------------|
Output -> Lett}$Tvskveqqmrk
```
See this becomes quite difficult to figure out the real meaning of the cipher text, unless we know the jump number. Now we can use the same method for encrypting the strings / files with a password. Only thing is that we have to convert the password string to a unique jump number.

* __Encryption algorithms :-__ There are many encryption algorithms created over time, you can also create your own encryption algorithms. But for now let me explain about encryption algorithms. Encryption algorithm is the process and way in which a piece of data is converted to a cipher data, in such way that only the application or the password used to encrypt is the only thing can revert the cipher data back to the original readable data. Some popular encryption algorithms are : RSA, AES, Triple DES, Blowfish, Twofish.

* __Hashing :-__  Hashing generates a unique signature of fixed length for a data set or message. Each specific message has its unique hash, making minor changes to the information easily trackable. Data encrypted with hashing cannot be deciphered or reversed back into its original form. That’s why hashing is used only as a method of verifying data. Many internet security experts don’t even consider hashing an actual encryption method, but the line is blurry enough to let the classification stand. The bottom line, it’s an effective way of showing that no one has tampered with the information.

## Why do we need Cryptography

You can skip this section if you do not want any other extra information. If anyone wonders why people and organizations need to practice encryption, keep these four reasons in mind:

* __Authentication :-__ Public key encryption proves that a website's origin server owns the private key and thus was legitimately assigned an SSL certificate. In a world where so many fraudulent websites exist, this is an important feature.

* __Privacy :-__ Encryption guarantees that no one can read messages or access data except the legitimate recipient or data owner. This measure prevents cybercriminals, hackers, internet service providers, spammers, and even government institutions from accessing and reading personal data.

* __Regulatory Compliance :-__ Many industries and government departments have rules in place that require organizations that work with users’ personal information to keep that data encrypted. A sampling of regulatory and compliance standards that enforce encryption include HIPAA, PCI-DSS, and the GDPR.

* __Security :-__ Encryption helps protect information from data breaches, whether the data is at rest or in transit. For example, even if a corporate-owned device is misplaced or stolen, the data stored on it will most likely be secure if the hard drive is properly encrypted. Encryption also helps protect data against malicious activities like man-in-the-middle attacks, and lets parties communicate without the fear of data leaks.


## Cryptography in Python

Python is very popular general programming language, which is used for writing the desktop applications, to server side applications. There are a ton of web and native applications written in python across the world. Many popular services which are used a billion of people everyday are powered by python backeneds. Thus it is extremely necessary to implement the encryption to the databases for the security purposes of the users. There are many python libraries providing very basic to advanced encryption algorithms, and also makes our coding less lengthy, but this would not make you a crypto expert. For that we need to learn to create an encryption algorithm on ourself. So first we need to understand on how we can convert a plain text to a unreadable form from a plain text password. Also we will make sure that the unreadable format text can be convertable using that password only. For that we can just generate a unique integer from the password text. The key hence generated can be used to jump the places for the char code in the plain text. First we need to write an algorithm for the creation of the key from a password text, also the key must be unique in atleast 10,000 different passwords. The password also will be used to revert back the encrypted text back to the plain format. Let us write the code.

## Writing the Code

Beggining with importing some modules. As we are not using any external libraries, only library that we need to import is the __hashlib__. But we will not just import the whole library, we will import the 2 functions and that are _b64encode_ and _b64decode_. We will use the below code :
```
from base64 import b64encode, b64decode
```
Now we will define a function __getKey()__ for the creation of a unique key out of a specific password combination as provided by the user. The function will return an integer type numeric key. We will use the below algorithm for that purpose. The code is as follows :
```
def getKey(password):
	"""
The function for the generation of unique key out of a password combination
	"""

	key = 0
        for i, j in enumerate(password):
                if i % 2 == 0:
                        key += ord(j)
                else:
                        key -= ord(j)
        if key < 0:
                key = key * (-1)
        key += len(password)
        return key
```
Lets break down the function getKey() into points :
* First we will define the function with the name and the required arguments that is the plain password.
* Now we will generate the key by iteration of each characters and calculating the char codes of the iterated characters. For the calculation we have a algorithm in which if we have an odd loop turn then we will subtract the char code from the key and for even loop turn, the char code will be added to the key.
* The key then comes out to be either a negative or a possitive integer. For making the negative key into possitive integer, we will multiply it with a -1, for making it possitive.
* Then to make the key larger and most possibly a bit larger than 0, we will add up the length of the password string to the key positive integer. The code is _key += len(password)_.

Now lets define two functions __encrypt()__ and __decrypt()__, and these functions does the same job as per their names. Both functions will take two arguments each and those arguments are the plain text and the password. The functions will be working on the same algorithm, only thing is that the decrypt() function will do the opposite sides of the algorithms. Lets write the _encrypt_ function first.
```
def encrypt(text, password):
	"""
The function for encrypting the plain text
	"""

	key = getKey(text)
	encryptedText = ""
	for i in text:
		encryptedText += chr((ord(i) + key) % 256)
	
	encryptedText = b64encode(encryptedText.encode()).decode()
	
	return encryptedText
```
Breaking down the statements and the structure of the encrypt() function :
* First we will define the encrypt function which takes two arguments _the plain text_ and the _password_. Now let us write the further statements in the function block.
* Then we will get the key by calling the getKey() function and save it to the key variable. We will use it to jump the steps in the plain text.
* Then we will declare an empty string variable which will contain the encrypted text so formed. Now lets write the loop to form the cipher character out of each character in the plain text.
* We will use the for loop to iterate over the characters and form a cipher randomized character with a simple algorithm applied to the char code. The algorithm is _(char code of character + numeric key) % 256_. We will add up the numeric key to the char code of the character and then find out the remainder with 256. We get the char code for the cipher character, we will use the chr() function to get the cipher character. We will add up the cipher character to the encryptedText variable.
* After the loop we will convert the encryptedText variable to a base64 encoded format string. We will use the code _encryptedText = b64encode(encryptedText.encode()).decode()_.

After encryption function we will move to __decrypt()__ function, the function will work opposite to the encrypt() function. Below is the code for the decrypt function :
```
def decrypt(text, password):
	"""
The function for decryption of already encrypted script
	"""

	text = b64decode(text.encode()).decode()
	key = getKey(password)
	decryptedText = ""
	for i in text:
		decryptedText += chr((ord(i) - key) % 256)
	return decryptedText
```
Lets break down the code for the function decrypt() :
* First we will declare the function with name _decrypt_ and it will take two arguments which are the encrypted text and the password.
* Then we will convert the base64 encoded text back to utf-8 (original) form. We will use the code _text = b64decode(text.encode()).decode()_.
* Now we will generate the key from the password argument using the getKey() function, in the same way that we used in the encrypt() function.
* Then we will declare an empty string variable with name _decryptedText_.
* We will use a for loop to iterate through the cipher text, and follow the same algorithm to generate character as we used in encrypt() function, but in case of decryption we will subtract instead of the adding the key. We will add up each plain formed character with the decryptedText string.
* At last we will return the plain string which is decryptedText.

Here we have completed writting the functions required for the making the encryption script. We can now simply make a menu based input script and use the encrypt() and decrypt() functions for the process. You can write the script part as shown in the video. Just pass the string and password of the encryption to the any of the functions and save the output to a variable.

## Conclusion

So at last we have learnt many terms and topics and their brief information, We also learnt to secure our private information using a simple python script and that too without using any external libraries. If you have any doubts or queries, you can contact me at my [instagram handle](https://instagram.com/rodfficial192/).

Below are some links useful for you :-
* Clearing python cache using shell script - [click here](https://www.youtube.com/watch?v=MB86rR9uzNo&t=16s)
* Cracking passwords using python - [click here](https://www.youtube.com/watch?v=316uQ6WyCTE&t=3s)
* Chat Bomber using just 20 lines of python code - [click here](https://www.youtube.com/watch?v=_DlxNy3KsDo)
