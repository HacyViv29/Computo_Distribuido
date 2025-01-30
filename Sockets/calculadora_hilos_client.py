import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999

# Conectar al servidor
client_socket.connect((host, port))

# Solicitar los dos números al usuario
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Enviar los números al servidor
client_socket.send(f"{num1} {num2}".encode('utf-8'))

# Recibir los cuatro resultados del servidor
resultados = client_socket.recv(1024).decode('utf-8')

# Mostrar los resultados al usuario
print("Resultados recibidos:")
print(resultados)

# Cerrar la conexión
client_socket.close()