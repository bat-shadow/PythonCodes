grade = input("Enter grade: ")

match grade.upper():
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Poor")
    case _:
        print("Fail")