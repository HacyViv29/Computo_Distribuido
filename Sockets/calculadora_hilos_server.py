import socket
import threading

# Función para realizar una operación específica
def calcular_operacion(num1, num2, operacion, resultados, indice):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operacion == '+':
            resultados[indice] = f"Suma: {num1 + num2}"
        elif operacion == '-':
            resultados[indice] = f"Resta: {num1 - num2}"
        elif operacion == '*':
            resultados[indice] = f"Multiplicación: {num1 * num2}"
        elif operacion == '/':
            if num2 == 0:
                resultados[indice] = "División: Error (división entre 0)"
            else:
                resultados[indice] = f"División: {num1 / num2}"
    except Exception as e:
        resultados[indice] = f"Error en la operación {operacion}: {str(e)}"

# Función para manejar cada cliente
def manejar_cliente(client_socket, addr):
    print(f"Conexión establecida con {addr}")
    
    # Recibir los dos números del cliente
    datos = client_socket.recv(1024).decode('utf-8')
    num1, num2 = datos.split()
    print(f"Números recibidos: {num1}, {num2}")
    
    # Lista para almacenar los resultados de las operaciones
    resultados = [None] * 4
    
    # Crear hilos para cada operación
    hilos = []
    operaciones = ['+', '-', '*', '/']
    for i, operacion in enumerate(operaciones):
        hilo = threading.Thread(target=calcular_operacion, args=(num1, num2, operacion, resultados, i))
        hilos.append(hilo)
        hilo.start()
    
    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()
    
    # Enviar los resultados al cliente
    resultados_str = "\n".join(resultados)
    client_socket.send(resultados_str.encode('utf-8'))
    
    # Cerrar la conexión con el cliente
    client_socket.close()
    print(f"Conexión con {addr} cerrada")

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
    
    # Crear un hilo para manejar la conexión del cliente
    cliente_thread = threading.Thread(target=manejar_cliente, args=(client_socket, addr))
    cliente_thread.start()