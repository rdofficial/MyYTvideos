# Importing the required modules
from base64 import b64encode, b64decode

def getKey(password):
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

def encrypt(text, password):
	""" The function to encrypt a string """

	key = getKey(password)
	encryptedText = ""
	for i in text:
		encryptedText += chr((ord(i) + key) % 256)
	encryptedText = b64encode(encryptedText.encode()).decode()
	return encryptedText

def decrypt(text, password):
	""" The function for decryption of a encrypted string """

	key = getKey(password)
	decryptedText = ""
	text = b64decode(text.encode()).decode()
	for i in text:
		decryptedText += chr((ord(i) - key) % 256)
	return decryptedText

# Asking the user for inputs
text = input('Enter something : ')
password = input('Enter the password : ')
choice = input("""Choose any of the below :
1. Encryption
2. Decryption

Enter your choice : """)

if choice == '1':
	# If the user chooses to encrypt

	text = encrypt(text, password)
elif choice == '2':
	# If the user chooses to decrypt

	text = decrypt(text, password)
else:
	# If the user chooses none

	print('No such option available')
	quit()

print('Result of operation : \n' + text)

