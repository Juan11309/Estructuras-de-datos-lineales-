arr=[345, 721, 425, 572, 836, 467, 672,194, 365, 236, 891, 746, 431, 834, 247, 529, 216, 389]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        # 10 buckets para decimal (0-9)
        buckets = [[] for _ in range(10)]

        # Distribuir cada número en su bucket según el dígito actual
        for num in arr:
            digito = (num // exp) % 10
            buckets[digito].append(num)

        # Recoger los buckets en orden
        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        exp *= 10  # siguiente dígito

    return arr
