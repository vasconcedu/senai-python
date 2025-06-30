def fib(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    elif n >= 2:
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[i-2] + seq[i-1])
        return seq

n = int(input("n> "))
print("fib({}) = {}".format(n, fib(n)))
