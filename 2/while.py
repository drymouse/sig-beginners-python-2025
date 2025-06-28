password = "password"

input_pw = input("Input password > ")

while input_pw != password:
    print("Not match")
    input_pw = input("Input password > ")

print("Match")