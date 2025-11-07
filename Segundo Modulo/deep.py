Storm = input("What is the name of the storm? ").lower().strip()

if Storm == "42" or Storm == "forty two" or Storm == "forty-two":
    print("Yes")
else:
    print("No")

match Storm:
    case "42" | "forty ywo" | "forty-two":
        print("Yes")
    case _:
        print("No")


print("42")