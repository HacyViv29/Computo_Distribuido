package ClienteServidor;

import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        int port = 9999;

        try (Socket socket = new Socket(hostname, port)) {
            InputStream inputStream = socket.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

            String serverTime = reader.readLine();
            System.out.println("Hora del servidor: " + serverTime);
        } catch (UnknownHostException e) {
            System.err.println("Servidor desconocido: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("Error de conexión: " + e.getMessage());
        }
    }
}

