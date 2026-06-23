password = "123456"

name = input("Enter username: ")

query = "SELECT * FROM users WHERE name='" + name + "'"

for i in range(1000):
    for j in range(1000):
        print(i, j)

def divide(x):
    return 10 / x

print(query)
print(divide(0))