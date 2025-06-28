fib = [0, 1] # fib(n) = fib[n]
print(fib[0])
print(fib[1])

i = 0
while i < 29:
    fib.append(fib[i+1] + fib[i])
    i += 1

print(fib)
