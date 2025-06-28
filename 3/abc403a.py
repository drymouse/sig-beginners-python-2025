N = int(input())
A = list(map(int, input().split()))

sum = 0

for i in range(0, N, 2):
    sum += A[i]

print(sum)