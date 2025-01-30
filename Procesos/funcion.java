public class funcion {
    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Uso: java funcion <number>");
            System.exit(1);
        }
        int i = Integer.parseInt(args[0]);
        System.out.println("calling funcion from process: " + i);
        for (int j = 0; j < i; j++) {
            System.out.println("output from funcion is :" + j);
        }
    }
}