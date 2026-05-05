import random
# funcion 1
codigos = [random.randint(1000, 9999) for _ in range(10)]
nombres = ["Ana", "Luis", "Sofia", "Juan", "Santiago", "Esteban", "Maria", "Pedro", "Valerie", "Diego"]
notas   = [[random.randint(10, 50) for _ in range(3)] for _ in range(10)] 

def definitiva(n):
    return n[0] * 0.30 + n[1] * 0.30 + n[2] * 0.40

# funcion 2
def busqueda_binaria(codigos, codigo):
    low = 0
    high = len(codigos) - 1

    while low <= high:
        mid = (low + high) // 2

        if codigos[mid] == codigo:
            return mid
        elif codigos[mid] < codigo:
            low = mid + 1
        else:
            high = mid - 1

    return -1
# funcion 3
for i in range(1, 10):
    key_cod   = codigos[i]
    key_nom   = nombres[i]
    key_notas = notas[i]
    key_prom  = definitiva(key_notas)
    j = i - 1

    while j >= 0 and definitiva(notas[j]) > key_prom:
        codigos[j + 1] = codigos[j]
        nombres[j + 1] = nombres[j]
        notas[j + 1]   = notas[j]
        j -= 1

    codigos[j + 1] = key_cod
    nombres[j + 1] = key_nom
    notas[j + 1]   = key_notas

# funcion 4
print("\n DATOS ORDENADOS")
print(f"{'Código':<8} {'Nombre':<12} {'N1':>4} {'N2':>4} {'N3':>4} {'Prom':>6}")
for i in range(10):
    print(f"{codigos[i]:<8} {nombres[i]:<12} {notas[i][0]:>4} {notas[i][1]:>4} {notas[i][2]:>4} {definitiva(notas[i]):>6.2f}")
