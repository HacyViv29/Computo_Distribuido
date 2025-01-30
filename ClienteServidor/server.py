import socket
import time

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()
port=9999

serversocket.bind((host,port))

serversocket.listen(5)

while True:
    clientsocket,addr=serversocket.accept()
    print("Connected with [addr], [port]%s"%str(addr))
    currenTime=time.ctime(time.time())+"\r\n"
    clientsocket.send(currenTime.encode('ascii'))
    clientsocket.close()