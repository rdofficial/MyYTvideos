# The script to get the IP address of a web server by its domain address ( like google.com )

# Importing the required functions from the required modules
from socket import gethostbyname

# Asking the user for the domain address
address = input('Enter the domain address : ')
try:
	ip = gethostbyname(address)
except Exception as e:
	print('[ Error : {} ]'.format(e))
else:
	print('The IP address is {}'.format(ip))
