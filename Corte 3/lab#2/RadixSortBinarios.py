lista_num=[345, 721, 425, 572, 836, 467, 672,194, 365, 236, 891, 746, 431, 834, 247, 529, 216, 389]

def radix_sort(lista_num):
    max_val = max(lista_num)
    exp = 1

    while max_val // exp > 0:
        # 10 buckets para decimal (0-9)
        buckets = [[] for _ in range(10)]

        # Distribuir cada número en su bucket según el dígito actual
        for num in lista_num:
            digito = (num // exp) % 10
            buckets[digito].append(num)

        # Recoger los buckets en orden
        lista_num = []
        for bucket in buckets:
            lista_num.extend(bucket)

        exp *= 10  # siguiente dígito

    return lista_num

resultado = radix_sort(lista_num)
print(resultado)
