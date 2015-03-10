import socket

#socket_family: This is either AF_UNIX or AF_INET, as explained earlier.
#socket_type: This is either SOCK_STREAM or SOCK_DGRAM
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
# Get local machine name & reserve a port
host = socket.gethostname()
#host = '192.168.1.64'
print host
port = 12345
s.bind((host, port))
# Now wait for client connection.
s.listen(5)
while True:
        # Establish connection with client.
        c, addr = s.accept()
        print 'Got connection from', addr
        #c.send(open('f.html').read())
        c.send('thank you for connecting')
        c.close()

