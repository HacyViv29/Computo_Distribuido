import socket

def calcular(operacion):
    try:
        # Dividir la operación en sus componentes (ejemplo: "5 + 3")
        partes = operacion.split()
        num1 = float(partes[0])
        operador = partes[1]
        num2 = float(partes[2])
        
        # Realizar el cálculo según el operador
        if operador == '+':
            return str(num1 + num2)
        elif operador == '-':
            return str(num1 - num2)
        elif operador == '*':
            return str(num1 * num2)
        elif operador == '/':
            if num2 == 0:
                return "Error: División entre 0"
            return str(num1 / num2)
        else:
            return "Error: Operador no válido"
    except Exception as e:
        return "Error: Operación no válida"

# Configuración del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # Obtener el nombre del host local
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Servidor escuchando en {host}:{port}")

while True:
    # Aceptar una conexión entrante
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida con {addr}")
    
    # Recibir la operación del cliente
    operacion = client_socket.recv(1024).decode('utf-8')
    print(f"Operación recibida: {operacion}")
    
    # Calcular el resultado
    resultado = calcular(operacion)
    print(f"Resultado: {resultado}")
    
    # Enviar el resultado de vuelta al cliente
    client_socket.send(resultado.encode('utf-8'))
    
    # Cerrar la conexión con el cliente
    client_socket.close()
