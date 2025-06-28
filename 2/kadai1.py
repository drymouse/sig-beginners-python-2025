prev = 1
pprev = 0

print(pprev)
print(prev)

i = 2
while i <= 30:
    i += 1

    tmp = prev
    prev = prev + pprev
    pprev = tmp
    print(prev)
