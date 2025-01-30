public class hilos2 extends Thread{
    @Override
    public void run() {
        System.out.println("Hola Mundo desde el hilo");
    }

    public static void main(String[] args) {
        hilos hilo = new hilos();
        Thread t = new Thread(hilo);
        t.start();
    }
}