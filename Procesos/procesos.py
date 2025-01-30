import multiprocessing
import time

def function(i):
    print("Ejecición del proceso n°: %s" %i)
    time.sleep(0.5)

if __name__ == '__main__':
    print("Inicio del proceso principal")
    process1 = multiprocessing.Process(target=function, args=("1",))
    process2 = multiprocessing.Process(target=function, args=("2",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Fin del proceso principal")