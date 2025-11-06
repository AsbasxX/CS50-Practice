def main():
    dollars = dollars_to_float(input("how much was the meal? "))
    percentage = percent_to_float(input("what percentage would you like to tip? "))
    tip = dollars * (percentage / 100)
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d.replace("$", ""))

def percent_to_float(p):
    return float(p.replace("%", ""))

main()