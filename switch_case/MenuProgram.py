print("1. Pizza")
print("2. Burger")
print("3. Pasta")

choice = int(input("Choose item: "))

match choice:
    case 1:
        print("You ordered Pizza")
    case 2:
        print("You ordered Burger")
    case 3:
        print("You ordered Pasta")
    case _:
        print("Invalid choice")