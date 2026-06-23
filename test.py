password = "admin123"

user_input = input("Enter username: ")

query = "SELECT * FROM users WHERE name='" + user_input + "'"

print(query)