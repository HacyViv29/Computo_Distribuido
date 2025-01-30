import threading

def hola_mundo():
    print("Hola Mundo desde el hilo!")

if __name__ == "__main__":
    hilo = threading.Thread(target=hola_mundo)
    hilo.start()
    hilo.join()
