global_var = 10

def test(arg):
    global global_var
    global_var = 20
    return arg * global_var

print(test(1))
print(test(10))

print(global_var)