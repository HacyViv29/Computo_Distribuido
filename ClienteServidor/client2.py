import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=60000



print('connection closed')