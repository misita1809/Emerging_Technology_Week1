# Write a python program which accepts the user's first and last name and print them in reverse order with a space between them

first_name=input("Enter your first name: ")

last_name=input("Enter your last name: ")

name = first_name+" "+last_name

print("Name: ",name)

Reverse = name[-1::-1]

print(f"Reverse name: {Reverse}")
