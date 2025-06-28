def fib_iter():
    yield 0
    yield 1
    a = 0
    b = 1
    while True:
        yield a + b
        a, b = b, a + b

if __name__ == "__main__":
    it = fib_iter()

    for i in range(30):
        print(next(it))
