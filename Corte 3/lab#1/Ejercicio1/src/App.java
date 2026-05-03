import java.util.Random;

public class App {
    public static void main(String[] args) {
 
        // N es un número aleatorio entre 10 y 20 (inclusive)
        Random rand = new Random();
        int n = rand.nextInt(11) + 10;
 
        System.out.println("Número de registros generados: " + n);
 
        // Crear el objeto con el tamaño definido
        GestionPedidos gestion = new GestionPedidos(n);
 
        // Llamar las funciones en el orden indicado
        gestion.funcion1();
        gestion.funcion2();
        gestion.funcion3();
    
    }
}
