// MainProgram.java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class procesos {
    public static void main(String[] args) {
        for (int i = 0; i < 6; i++) {
            ProcessBuilder processBuilder = new ProcessBuilder("java", "funcion", String.valueOf(i));
            try {
                Process process = processBuilder.start();

                // Captura y muestra la salida del proceso
                printStream(process.getInputStream());

                process.waitFor();
            } catch (IOException | InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private static void printStream(InputStream inputStream) {
        new BufferedReader(new InputStreamReader(inputStream)).lines()
                .forEach(System.out::println);
    }
}