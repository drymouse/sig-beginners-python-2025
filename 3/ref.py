# 参照渡し

l1 = [1, 2, 3, 4]
l2 = l1

print("l1", l1)
print("l2", l2)

l1.append(5)

print("l1", l1)
print("l2", l2)

# 値渡し

v1 = 10
v2 = v1

print("v1", v1)
print("v2", v2)

v1 = 11

print("v1", v1)
print("v2", v2)

import copy

l1 = [1, 2, 3, 4]
l2 = copy.deepcopy(l1)

print("l1", l1)
print("l2", l2)

l1.append(5)

print("l1", l1)
print("l2", l2)