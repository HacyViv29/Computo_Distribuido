import socket
port=60000
s=socket.socket()
host=socket.gethostname()
s.bind((host, port))
s.listen(15)
print('Server Listening...')
while True:
    conn,addr=s.accept()
    print('Got connection from', addr)
    data=conn.recv(1824)
    print('Server received',repr(data.decode()))
    filename='mytext.txt'
    f=open(filename,'rb')
    l=f.read(1824)
    while (l):
        conn.send()
        print('Sent', repr(l.decode()))
        l=f.read()
        f.close()
        print ('Done sending')
        conn.send('->Thanks you for connecting'.encode())
        conn.close()