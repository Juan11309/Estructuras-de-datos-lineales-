import java.util.Random;
import java.util.Arrays;

public class GestionPedidos {


    private int[] producto;
    private int[] cantidad;
    private int[] precio;
    private int n; // número de registros

   
    private int[]    prodUnico;
    private int[]    totalCantidad;
    private double[] precioPromedio;
    private int      cantUnicos; // cuántos productos únicos se encontraron

    public GestionPedidos(int n) {
        this.n = n;

        this.producto = new int[n];
        this.cantidad = new int[n];
        this.precio   = new int[n];

        this.prodUnico      = new int[n];
        this.totalCantidad  = new int[n];
        this.precioPromedio = new double[n];
        this.cantUnicos     = 0;
    }


    // FUNCIÓN 1: Poblar 
    public void funcion1() {

        Random rand = new Random();

        // Códigos de producto disponibles
        int[] codigos = {1010, 1020, 1030, 1040, 1050, 1060};

        for (int i = 0; i < n; i++) {
            // Elegir un código de producto al azar
            producto[i] = codigos[rand.nextInt(codigos.length)];

            // Cantidad entre 1 y 50
            cantidad[i] = rand.nextInt(50) + 1;

            // Precio entre 10 y 30
            precio[i] = rand.nextInt(21) + 10;
        }

        
        // Mostrar los arreglos generados para verificar
        System.out.println("\n--- Datos generados (entrada) ---");
        System.out.println("Producto : " + Arrays.toString(producto));
        System.out.println("Cantidad : " + Arrays.toString(cantidad));
        System.out.println("Precio   : " + Arrays.toString(precio));
    }


    // FUNCIÓN 2: Agrupar por código, sumar cantidades y calcular el precio promedio por producto
        public void funcion2() {
    ordenarOriginales();

    int sumaPrecios   = 0;
    int contadorVeces = 0;

    for (int i = 0; i < n; i++) {


        sumaPrecios   += precio[i];
        contadorVeces++;

        if (i == n - 1 || producto[i] != producto[i + 1]) {
            prodUnico[cantUnicos]     = producto[i];
            totalCantidad[cantUnicos] = 0;

            // Sumar todas las cantidades de este grupo
            for (int k = i - contadorVeces + 1; k <= i; k++) {
                totalCantidad[cantUnicos] += cantidad[k];
            }

            // Calcular el precio promedio de este grupo
            precioPromedio[cantUnicos] = (double) sumaPrecios / contadorVeces;

            cantUnicos++;

            // Reiniciar acumuladores para el siguiente grupo
            sumaPrecios   = 0;
            contadorVeces = 0;
        }
    }
}

private void ordenarOriginales() {

    for (int i = 0; i < n - 1; i++) {

        int posMinimo = i;
        for (int j = i + 1; j < n; j++) {
            if (producto[j] < producto[posMinimo]) {
                posMinimo = j;
            }
        }

        int tempProd = producto[i];
        producto[i] = producto[posMinimo];
        producto[posMinimo] = tempProd;

        int tempCant = cantidad[i];
        cantidad[i] = cantidad[posMinimo];
        cantidad[posMinimo] = tempCant;

        int tempPrecio = precio[i];
        precio[i] = precio[posMinimo];
        precio[posMinimo] = tempPrecio;
    }
}

    public void funcion3() {

        System.out.println("\n===== RESULTADOS =====");
        System.out.printf("%-12s %-16s %-16s%n", "Producto", "Total Cantidad", "Precio Promedio");
        System.out.println("----------------------------------------------");

        int    sumaTotalCantidad  = 0;
        double sumaPrecioPromedio = 0;

        for (int i = 0; i < cantUnicos; i++) {
            System.out.printf("%-12d %-16d %.2f%n",
                    prodUnico[i], totalCantidad[i], precioPromedio[i]);

            sumaTotalCantidad  += totalCantidad[i];
            sumaPrecioPromedio += precioPromedio[i];
        }

        System.out.println("Suma total de cantidades : " + sumaTotalCantidad);
        System.out.printf("Promedio de venta general: %.2f%n", sumaPrecioPromedio / cantUnicos);
    }
}
