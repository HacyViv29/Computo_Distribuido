import socket

# Configuración del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()  # Debe coincidir con el host del servidor
host = "172.26.163.92"
port = 9999

# Conectar al servidor
client_socket.connect((host, port))

# Solicitar operación al usuario
print("Ingrese la operación en el formato: número1 operador número2 (ej: 5 + 3)")
operacion = input("Operación: ")

# Enviar la operación al servidor
client_socket.send(operacion.encode('utf-8'))

# Recibir el resultado del servidor
resultado = client_socket.recv(1024).decode('utf-8')

print(f"Resultado: {resultado}")

# Cerrar la conexión
client_socket.close()
