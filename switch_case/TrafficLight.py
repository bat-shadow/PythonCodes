color = input("Enter traffic color: ")

match color.lower():
    case "red":
        print("Stop")
    case "yellow":
        print("Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid")