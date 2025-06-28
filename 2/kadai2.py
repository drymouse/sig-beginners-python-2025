import random

n = 1000000 # この値をいろいろ変えてみよう

array = [random.randint(-pow(2, 20), pow(2, 20)-1) for _ in range(n)]
array = sorted(array)

print("array generated!")
# print(array)
# この下に二分探索のプログラムをかいてください

target = int(input("Enter a number > "))

a = 0
b = n - 1

found = False

while a <= b:
    c = (a + b) // 2
    if target == array[c]:
        print("Yes")
        found = True
        break
    elif target < array[c]:
        b = c - 1
    else:
        a = c + 1

if not found:
    print("No")