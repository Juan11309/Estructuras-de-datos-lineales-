import random

def definitiva(n):
    return n[0] * 0.30 + n[1] * 0.30 + n[2] * 0.40

# Función 1
def poblar():
    codigos = [random.randint(1000, 9999) for _ in range(10)]
    nombres = ["Ana", "Luis", "Sofia", "Juan", "Santiago", "Esteban", "Maria", "Pedro", "Valerie", "Diego"]
    notas   = [[random.randint(10, 50) for _ in range(3)] for _ in range(10)]
    return codigos, nombres, notas  # ← eliminado el return duplicado

# Función 2
def ordenar(codigos, nombres, notas):
    for i in range(1, 10):
        key_cod   = codigos[i]
        key_nom   = nombres[i]
        key_notas = notas[i]
        key_prom  = definitiva(key_notas)
        j = i - 1

        while j >= 0 and definitiva(notas[j]) < key_prom:  # ← indentado dentro del for
            codigos[j + 1] = codigos[j]
            nombres[j + 1] = nombres[j]
            notas[j + 1]   = notas[j]
            j -= 1

        codigos[j + 1] = key_cod  # ← indentado dentro del for
        nombres[j + 1] = key_nom
        notas[j + 1]   = key_notas

# Función 3
def busqueda_binaria(codigos, nombres, notas, codigo_buscado):  # ← parámetros completos
    indices = sorted(range(len(codigos)), key=lambda i: codigos[i])
    cod_ord = [codigos[i] for i in indices]

    low, high = 0, len(cod_ord) - 1

    while low <= high:
        mid = (low + high) // 2
        if cod_ord[mid] == codigo_buscado:
            idx = indices[mid]
            print(f"\n Estudiante encontrado:")
            print(f"  Código    : {codigos[idx]}")
            print(f"  Nombre    : {nombres[idx]}")
            print(f"  Nota 1    : {notas[idx][0]}")
            print(f"  Nota 2    : {notas[idx][1]}")
            print(f"  Nota 3    : {notas[idx][2]}")
            print(f"  Definitiva: {definitiva(notas[idx]):.2f}")
            return
        elif cod_ord[mid] < codigo_buscado:
            low = mid + 1
        else:
            high = mid - 1

    print(f"\n Código {codigo_buscado} no encontrado.")

# Función 4
def mostrar(codigos, nombres, notas):
    print("\n DATOS ORDENADOS")
    print(f"{'Código':<8} {'Nombre':<12} {'N1':>4} {'N2':>4} {'N3':>4} {'Prom':>6}")
    for i in range(10):
        print(f"{codigos[i]:<8} {nombres[i]:<12} {notas[i][0]:>4} {notas[i][1]:>4} {notas[i][2]:>4} {definitiva(notas[i]):>6.2f}")

# Test
codigos, nombres, notas = poblar()
ordenar(codigos, nombres, notas)
mostrar(codigos, nombres, notas)
