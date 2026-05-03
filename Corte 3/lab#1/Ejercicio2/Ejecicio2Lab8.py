import random

def poblar(codigos, nombres, notas):
    pool = ["Ana","Luis","Sofia","Juan","Maria","Carlos","Laura","Pedro","Valeria","Diego"] #funcion 1
    for i in range(len(codigos)):
        codigos[i]  = random.randint(1000, 9999)
        nombres[i]  = pool[i]
        notas[i][0] = round(random.uniform(1.0, 5.0), 2)
        notas[i][1] = round(random.uniform(1.0, 5.0), 2)
        notas[i][2] = round(random.uniform(1.0, 5.0), 2)
        notas[i][3] = round(notas[i][0]*0.30 + notas[i][1]*0.30 + notas[i][2]*0.40, 2)

def quicksort_codigo(codigos, nombres, notas, ini, fin):# QuickSort por código ASCENDENTE 
    if ini >= fin:
        return
    pivote = codigos[fin]
    i = ini - 1
    for j in range(ini, fin):
        if codigos[j] <= pivote:
            i += 1
            codigos[i], codigos[j] = codigos[j], codigos[i]
            nombres[i], nombres[j] = nombres[j], nombres[i]
            notas[i],   notas[j]   = notas[j],   notas[i]
    i += 1
    codigos[i], codigos[fin] = codigos[fin], codigos[i]
    nombres[i], nombres[fin] = nombres[fin], nombres[i]
    notas[i],   notas[fin]   = notas[fin],   notas[i]
    quicksort_codigo(codigos, nombres, notas, ini, i - 1)
    quicksort_codigo(codigos, nombres, notas, i + 1, fin)

def quicksort_def_desc(codigos, nombres, notas, ini, fin): # QuickSort por definitiva DESCENDENTE
    if ini >= fin:
        return
    pivote = notas[fin][3]
    i = ini - 1
    for j in range(ini, fin):
        if notas[j][3] >= pivote:
            i += 1
            codigos[i], codigos[j] = codigos[j], codigos[i]
            nombres[i], nombres[j] = nombres[j], nombres[i]
            notas[i],   notas[j]   = notas[j],   notas[i]
    i += 1
    codigos[i], codigos[fin] = codigos[fin], codigos[i]
    nombres[i], nombres[fin] = nombres[fin], nombres[i]
    notas[i],   notas[fin]   = notas[fin],   notas[i]
    quicksort_def_desc(codigos, nombres, notas, ini, i - 1)
    quicksort_def_desc(codigos, nombres, notas, i + 1, fin)

def ordenar_por_codigo(codigos, nombres, notas): #funcion 2
    quicksort_codigo(codigos, nombres, notas, 0, len(codigos) - 1)

def buscar_por_codigo(codigos, nombres, notas, codigo_buscado): #funcion 3
    bajo, alto, pos = 0, len(codigos) - 1, -1
    while bajo <= alto:
        mid = (bajo + alto) // 2
        if   codigos[mid] == codigo_buscado: pos = mid; break
        elif codigos[mid] <  codigo_buscado: bajo = mid + 1
        else:                                alto = mid - 1
    if pos == -1:
        print("Codigo", codigo_buscado, "no encontrado.")
    else:
        print("Codigo:",     codigos[pos])
        print("Nombre:",     nombres[pos])
        print("Parcial 1:",  notas[pos][0])
        print("Parcial 2:",  notas[pos][1])
        print("Parcial 3:",  notas[pos][2])
        print("Definitiva:", notas[pos][3])

def mostrar_por_definitiva(codigos, nombres, notas): #funcion 4
    quicksort_def_desc(codigos, nombres, notas, 0, len(codigos) - 1)
    print("\nCodigo | Nombre     | P1   | P2   | P3   | Definitiva")

    for i in range(len(codigos)):
        print(codigos[i], "|", nombres[i], "|", notas[i][0], "|", notas[i][1], "|", notas[i][2], "|", notas[i][3])

N = 10
codigos = [0] * N
nombres = [""] * N
notas   = [[0.0] * 4 for _ in range(N)]

poblar(codigos, nombres, notas)

mostrar_por_definitiva(codigos, nombres, notas)

ordenar_por_codigo(codigos, nombres, notas)

print("\nBusqueda codigo existente:", codigos[N // 2])
buscar_por_codigo(codigos, nombres, notas, codigos[N // 2])

print("\nBusqueda codigo inexistente: 9999")
buscar_por_codigo(codigos, nombres, notas, 9999)