# Cracking passwords using python

This is the extended description / documentation for the video on my youtube channel, if you haven't watched the video yet then, [click here](https://www.youtube.com/watch?v=316uQ6WyCTE). There are more such interesting programming related videos in the playlist ["Cool Programming"](https://www.youtube.com/playlist?list=PLF0q9F-Pswkz1TrAhClq68w-4OLT3W4hQ), of which this video is a part of. To preview the source code, [click here](../data/password-cracker). Below starts the documentation.

__What to do :-__ In this tutorial, we are going to create a python script to crack hashed passwords of common algorithms. The script that we are going to make uses the dictionary attack format to check out the dictionary password against the hash provided by the user. We will make the use of the hashlib library for the hashing algorithms and pre built functions.

__Modules required :__ All the modules required by the script are pre installed or available in the default python library. The required modules are : ___hashlib___, and the script also required path module from the os library for verification of the wordlist file.

### Basic functions of hashlib module

The hashlib module is a pre installed python library for password hashing and undecryptable cryptography. There are various algorithms provided by the hashlib module, they are :
* md5
* sha1
* sha224
* sha256
* sha384
* sha512

There are many other algorithms, but they are not properly used. But you could use them in your custom script using the same methods as we will use for the basic algorithms. To use the functions in the module in our script, we will first import the hashlib module into our script.
```
import hashlib
```
There are functions with the same name for converting a plain text to a hashed cipher text. Also remember that the hashed text is required to be converted into ASCII format from raw bit wise data, generally any function like the md5() or sha1() returns the cipher data in form of bytes, and in order to do a real world application of the hash, we need to convert it to a text (ASCII) format, thus we will use a method called hexdigest() for converting the hex values back to the ASCII format. Below is a method to convert a simple text "passkey" to a md5 hash.
```
# THIS IS THE REQUIRED STR TEXT
text = "passkey"

# CONVERTING THE STR OBJECT TO A BYTES ONE
text = text.encode()

# MAKING THE HASH OF THE PLAIN TEXT WHICH IS IN BYTES FORMAT
hashedText = hashlib.md5(text).hexdigest()

# We have stored the hash of the variable "text" to a variable "hashedText"
```
Using the similar process, we will do the hashing for the other provided algorithms. Until know we have discussed about the basics of the hashlib library, lets us type the password cracker script.

### The structure of the script

The password cracker uses the dictionary attack format, that means the structure or the flow of the script is as below :
* First ask the user about the hashed formed of the password
* Ask the user for the wordlist file location ( The file which contains the passwords that are needed to be tried )
* Extracting the passwords from the wordlist that are needed to be tried.
* Using a loop to convert each plain password to hash format in order to verify wheter the original hash matches the current password's hash. If the hash matches, then break the loop and print success, else continue until the end of the loop.

The script must run without any errors and stoppage, so we would try to eradicate the error and dirty coding as much as possible and keep the script short and simple. Insert the try..except.. block wherever you feel to insert, and I let it on yourself for doing it.

The wordlist contain passwords in a format like one password each line, and this automatically adds up a '\n' character to the end of each password. So we would try to remove the escape sequence at the end of each password, also we will put the passwords to be tried into a dictionary object for faster execution of the loop.

### Writing the script

Lets start the password cracker script, I will use the nano console editor, you can use any other RAM consuming IDEs. Let me write the script in steps.
* __Importing the required module :-__ First of all, we will start with importing the required functions and modules to our script.
```
# Importing the required modules
import hashlib as hash
from os import path
```

* __Defining the main function :-__ We will define the main function of the script, I know it is not how python scripts are written generally, but I am a C addict, LOL!, Let us type the format, add the below code.
```
def main():
	""" The main function of the script """

    # Further statements
try:
	main()
except KeyboardInterrupt:
	quit()
```

Note that we are calling the main function in a try..except.. block. The reason to do is simple, whenever the user presses CTRL+C in between of the execution of the script, the script automatically stops itself and exits.

* __Asking the user for required inputs :-__ Now we will proceed into asking the user about the required inputs for the proper execution of the script. First we are going to ask the user about the original hash of the password which we have to crack. Then we will also ask for the location of the wordlist file.

```
hashedPassword = input('Enter the hashed password : ')
wordlist = input('Enter the wordlist file location : ')
```
Now we will also verify wheter the user entered wordlist file location exists or not, we will use the isfile() function from the path module in the os library. We will use the below code :
```
# Asking the user for required inputs
hashedPassword = input('Enter the hashed password : ')
wordlist = input('Enter the wordlist file location : ')

# Checking if the user specified wordlist exists or not
if path.isfile(wordlist):
    # If the user specified wordlist file exists
    
    # Statements for further scripts
else:
    # If the user specified wordlist file does not exists
    
    print('[ Error : No such file {} ]'.format(wordlist)
    quit()
```

* __Extracting the passwords from the wordlist file :-__ Now we will proceed to extract the passwords contained in the user specified wordlist file. We will contain all the extracted passwords in a dictionary object. The main reason for the extraction of the passwords is for removing the automatically added escape sequence '\n'. Below code needs to be inserted inside the if block.
```
# Reading the wordlist file
data = open(wordlist, 'r').read()
#
# Extracting the passwords and appending them to a list
passwords = []
for password in data:
    text = ''
    for i in password:
        # Removing the escape sequence from the each password
        if i == '\n':
            break
        else:
            text += i
    passwords.append(text)
```

* __Hashing each passwords in the list :-__ After we have extracted all the passwords from the wordlist file, we will proceed to hashing each password in the list using a loop. Before hashing each plain password, we need to convert the utf encoded string to a byte format. We will use the for loop for this purpose. Below code should be appended inside the if block.
```
# Hashing each passwords in the list
for password in passwords:
    
    # Converting the string password to a byte format
    password = password.encode()

    # Creating the hash from each algorithm
    md5_hash = hash.md5(password).hexdigest()
    sha1_hash = hash.sha1(password).hexdigest()
    sha224_hash = hash.sha224(password).hexdigest()
    sha256_hash = hash.sha256(password).hexdigest()
    sha384_hash = hash.sha384(password).hexdigest()
    sha512_hash = hash.sha512(password).hexdigest()
```

* __Verifying the hash of each algorithm :-__ Now as per we have proceeded the hashing algorithm of each plain password, and we have the hashed form of the password. We need to compare the user provided hashed password to these hashes. If any matches then we break the loop after printing the real passwords.
```
# Hashing each passwords in the list
for password in passwords:
    
    # Converting the string password to a byte format
    password = password.encode()

    # Creating the hash from each algorithm
    md5_hash = hash.md5(password).hexdigest()
    sha1_hash = hash.sha1(password).hexdigest()
    sha224_hash = hash.sha224(password).hexdigest()
    sha256_hash = hash.sha256(password).hexdigest()
    sha384_hash = hash.sha384(password).hexdigest()
    sha512_hash = hash.sha512(password).hexdigest()
    
    # Checking the hashes
    if md5_hash == hashedPassword or sha1_hash == hashedPassword or sha224_hash == hashedPassword or sha256_hash == hashedPassword or sha384_hash == hashedPassword or sha512_hash == hashedPassword:
        # If any hashes matches, we print the real password and break the loop
        
        print('[ Password found : {} ]'.format(password.decode())
        break
    else:
        # If the hashed does not matches, then we continue to next password try
        
        print('[ Password invalid : {} ]'.format(password.decode())
        continue
```
Thus we have created the complete password cracker script in python using just plain libraries without the help of any external libraries.

### Conclusion

We have completed the script, now lets test the script that we wrote. We can improve the scripts by adding colors, eradicating certain errors, also we can add more algorithms for cracking. That's all modifications on you.

The complete source code for the script is at [click here](../data/password-cracker)

The practical youtube video for this tutorial [click here](https://www.youtube.com/watch?v=316uQ6WyCTE)

If any more further queries, then can contact me at my [instagram handle](https://instagram.com/rdofficial192)

Below are some links useful for you :
[$] Colored outputs using python : [Click here](https://www.youtube.com/watch?v=ve_LP9tEozc)
[$] Installing python in android : [Click here]()https://www.youtube.com/watch?v=qzjt2PFdT6U
[$] Cracking passwords using python : [Click here](https://www.youtube.com/watch?v=316uQ6WyCTE)
