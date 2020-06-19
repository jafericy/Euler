def multiples(n1, n2, N):
    for n in range(N):
        if not n % n1 or not n % n2:
            yield n

q = sum(multiples(3,5,1000))

