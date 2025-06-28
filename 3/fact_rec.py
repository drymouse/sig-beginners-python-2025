def fact_rec(n):
    print("fact_rec called!:", n)
    if n == 0:
        return 1
    else:
        return n * fact_rec(n - 1)

print(fact_rec(4))