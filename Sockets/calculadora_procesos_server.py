import socket
from multiprocessing import Process, Queue

# Función para realizar una operación específica
def calcular_operacion(num1, num2, operacion, cola_resultados):
    try:
        num1 = float(num1)
        num2 = float(num2)
        if operacion == '+':
            resultado = f"Suma: {num1 + num2}"
        elif operacion == '-':
            resultado = f"Resta: {num1 - num2}"
        elif operacion == '*':
            resultado = f"Multiplicación: {num1 * num2}"
        elif operacion == '/':
            if num2 == 0:
                resultado = "División: Error (división entre 0)"
            else:
                resultado = f"División: {num1 / num2}"
        cola_resultados.put(resultado)  # Almacenar el resultado en la cola
    except Exception as e:
        cola_resultados.put(f"Error en la operación {operacion}: {str(e)}")

# Función para manejar cada cliente en un proceso separado
def manejar_cliente(client_socket, addr):
    print(f"Conexión establecida con {addr}")
    
    # Recibir los dos números del cliente
    datos = client_socket.recv(1024).decode('utf-8')
    num1, num2 = datos.split()
    print(f"Números recibidos: {num1}, {num2}")
    
    # Cola para almacenar los resultados de las operaciones
    cola_resultados = Queue()
    
    # Crear procesos para cada operación
    procesos = []
    operaciones = ['+', '-', '*', '/']
    for operacion in operaciones:
        proceso = Process(target=calcular_operacion, args=(num1, num2, operacion, cola_resultados))
        procesos.append(proceso)
        proceso.start()
    
    # Esperar a que todos los procesos terminen
    for proceso in procesos:
        proceso.join()
    
    # Recopilar los resultados de la cola
    resultados = []
    while not cola_resultados.empty():
        resultados.append(cola_resultados.get())
    
    # Enviar los resultados al cliente
    resultados_str = "\n".join(resultados)
    client_socket.send(resultados_str.encode('utf-8'))
    
    # Cerrar la conexión con el cliente
    client_socket.close()
    print(f"Conexión con {addr} cerrada")

# Configuración del servidor
def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()  # Obtener el nombre del host local
    port = 9999
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Servidor escuchando en {host}:{port}")

    while True:
        # Aceptar una conexión entrante
        client_socket, addr = server_socket.accept()
        
        # Crear un proceso para manejar la conexión del cliente
        cliente_process = Process(target=manejar_cliente, args=(client_socket, addr))
        cliente_process.start()

        # Cerrar el socket en el proceso principal para evitar conflictos
        client_socket.close()

if __name__ == "__main__":
    iniciar_servidor()