password = "password"

input_pw = input("Input password > ")

count = 1

while input_pw != password:
    print("Not match")
    if count == 3:
        break
    input_pw = input("Input password > ")
    count += 1 # count = count + 1

print("end")