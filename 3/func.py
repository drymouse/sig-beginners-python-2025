num_momo = 4
num_mikan = 10

def fruit_price(num_momo, num_mikan, num_ringo=0):
    total_momo = num_momo * 100
    total_mikan = num_mikan * 40
    total_ringo = num_ringo * 150
    total = total_momo + total_mikan + total_ringo
    return total

total = fruit_price(num_momo, num_mikan)

print(total)

print(fruit_price(10, 1))
print(fruit_price(num_mikan=10, num_momo=1))
print(fruit_price(10, 1, num_ringo=1))