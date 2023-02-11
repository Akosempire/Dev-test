#  Program to know the country users has visited by their inputs
print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, 'l' to list country visited or 'q' to quit: ")
country_visited = [ ]
while user_input != "q":
    print(input("Enter 'a' to add a country you've visited, 'l' to list country visited or 'q' to quit: "))
    if user_input == "a":
        input("enter the country you have visited: ")
        country_visited.append(user_input)

    else:
        print(country_visited)
