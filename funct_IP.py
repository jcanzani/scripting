
import socket

def obetner_ip():
	hostname = socket.gethostname()
	IPAddress = socket.gethostbyname(hostname)
	print ("Your computer is: " + hostname)
	print ("your IP Address is: " + IPAddress)

obetner_ip()
