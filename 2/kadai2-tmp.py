import random

n = 100 # この値をいろいろ変えてみよう

array = [random.randint(-pow(2, 20), pow(2, 20)-1) for _ in range(n)]
array = sorted(array)

print("array generated!")
# print(array) # arrayの中身を知りたいときはこのコメントアウトを外してください

# この下に二分探索のプログラムをかいてください
