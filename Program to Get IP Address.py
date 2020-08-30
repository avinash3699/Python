# Python Program to Get Computer Name and IP Address

from socket import gethostname,gethostbyname

computer_name = gethostname() 
IP_address = gethostbyname(computer_name)

print("Your Computer Name is: " + computer_name) 
print("Your Computer IP Address is: " + IP_address) 
