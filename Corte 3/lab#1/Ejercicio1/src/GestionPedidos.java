import java.util.Random;

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


    // FUNCIÓN 1: Poblar los arreglos con datos aleatorios
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
        System.out.print("Producto : ");
        for (int i = 0; i < n; i++) System.out.print(producto[i] + " ");
        System.out.print("\nCantidad : ");
        for (int i = 0; i < n; i++) System.out.print(cantidad[i] + " ");
        System.out.print("\nPrecio   : ");
        for (int i = 0; i < n; i++) System.out.print(precio[i] + " ");
        System.out.println();
    }


    // FUNCIÓN 2: Agrupar por código, sumar cantidades y calcular el precio promedio por producto
        public void funcion2() {

        // Arreglos auxiliares (solo se necesitan aquí adentro)
        int[] sumaPrecios   = new int[n];
        int[] contadorVeces = new int[n];

        // Recorrer todos los registros
        for (int i = 0; i < n; i++) {

            // Buscar si el código ya fue registrado en prodUnico
            int pos = -1;
            for (int j = 0; j < cantUnicos; j++) {
                if (prodUnico[j] == producto[i]) {
                    pos = j;
                    break;
                }
            }

            if (pos == -1) {
                // Es un producto nuevo → agregar
                prodUnico[cantUnicos]     = producto[i];
                totalCantidad[cantUnicos] = cantidad[i];
                sumaPrecios[cantUnicos]   = precio[i];
                contadorVeces[cantUnicos] = 1;
                cantUnicos++;
            } else {
                // El producto ya existe → acumular
                totalCantidad[pos] += cantidad[i];
                sumaPrecios[pos]   += precio[i];
                contadorVeces[pos]++;
            }
        }

        // Calcular el precio promedio para cada producto único
        for (int i = 0; i < cantUnicos; i++) {
            precioPromedio[i] = (double) sumaPrecios[i] / contadorVeces[i];
        }

        // Ordenar los tres arreglos por código de producto
        ordenarPorProducto();
    }

    // =========================================================
    // SELECTION SORT: Ordena los 3 arreglos por código de
    //                 producto de menor a mayor.
    //                 Es privado porque es un método de apoyo
    //                 interno, no lo necesita llamar el Main.
    // =========================================================
    private void ordenarPorProducto() {

        for (int i = 0; i < cantUnicos - 1; i++) {

            // Encontrar el índice del menor código a partir de i
            int posMinimo = i;
            for (int j = i + 1; j < cantUnicos; j++) {
                if (prodUnico[j] < prodUnico[posMinimo]) {
                    posMinimo = j;
                }
            }

            // Intercambiar en los 3 arreglos para mantener consistencia
            int tempProd = prodUnico[i];
            prodUnico[i] = prodUnico[posMinimo];
            prodUnico[posMinimo] = tempProd;

            int tempCant = totalCantidad[i];
            totalCantidad[i] = totalCantidad[posMinimo];
            totalCantidad[posMinimo] = tempCant;

            double tempPrecio = precioPromedio[i];
            precioPromedio[i] = precioPromedio[posMinimo];
            precioPromedio[posMinimo] = tempPrecio;
        }
    }

    // =========================================================
    // FUNCIÓN 3: Mostrar los resultados por consola
    // =========================================================
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

        System.out.println("----------------------------------------------");
        System.out.println("Suma total de cantidades : " + sumaTotalCantidad);
        System.out.printf("Promedio de venta general: %.2f%n", sumaPrecioPromedio / cantUnicos);
    }
}
