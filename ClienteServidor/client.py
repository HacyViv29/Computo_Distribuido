import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
#host = "172.26.165.144"
port = 9999

s.connect((host, port))

tm = s.recv(1824)

s.close()
print("Time connection server: %s" % tm.decode('ascii'))
