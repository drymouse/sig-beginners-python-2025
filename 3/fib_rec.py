def fib_rec(n):
    print("fib_rec called!:", n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

# print(fib_rec(50))

def fib_memo(n, memo): # memo[i] = fib(i)
    if len(memo) >= n + 1:
        return memo[n]
    if n == 0:
        memo.append(0)
        return 0
    elif n == 1:
        memo.append(1)
        return 1
    else:
        result = fib_memo(n-2, memo) + fib_memo(n-1, memo)
        memo.append(result)
        return result

l = []

print(fib_memo(10000, l))
# print(l)