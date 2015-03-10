import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		# Create a socket object
#host = '192.168.1.64'					# Get local machine name
host = socket.gethostbyname('raspberrypi')
#host = socket.gethostbyname('aj-pc')
#host = 'aj-pc'
#two last hosts are the same

print host
port = 12345							# Reserve a port for your service.


s.connect((host, port))
print s.recv(512)
s.close								# Close the socket when done
