MIDNIGHT = 0
BREAKFAST_START = 7
BREAKFAST_END = 8
MIDDAY = 12
LUNCH_END = 13
DINNER_START = 18
DINNER_END = 19
END_OF_DAY = 23


def main():
    """Ask which time format to use and dispatch processing.

    Keeps behavior simple: user selects 1 for 12-hour input or 2 for 24-hour input.
    Input is validated to avoid a crash when non-integers are entered.
    """
    try:
        time_format = int(input("Which format will you use?\n1) 12h\n2) 24h\nChoose 1 or 2: ").strip())
    except ValueError:
        print("Invalid option. Please enter 1 or 2.")
        return
    process(time_format)


def convert_12h(time12h):
    """Parse a 12-hour time string like "hh:mm a.m" or "h:mm pm" and call check_meal_time.

    Accepts variations with or without dots in the period (am/pm, a.m./p.m.).
    Performs validation on hours and minutes and converts to 24-hour hour integer.
    """
    s = time12h.strip().lower()
    # Expect a space between the time and period (e.g. "07:30 a.m")
    try:
        time_part, period = s.rsplit(" ", 1)
        hours_str, minutes_str = time_part.split(":")
    except ValueError:
        print('Invalid time format. Please use "hh:mm a.m/p.m".')
        return

    # Normalize and validate numeric parts
    try:
        hours = int(hours_str)
        minutes = int(minutes_str)
    except ValueError:
        print("Invalid hour or minute. Use numbers like 7:30 or 12:05.")
        return

    # Normalize period (accept am, a.m., pm, p.m.)
    period = period.replace('.', '')
    if period not in ("am", "pm"):
        print('Invalid period. Please use "a.m" or "p.m" (or am/pm).')
        return

    if not (1 <= hours <= 12):
        print("Invalid hour for 12h format. Hour must be between 1 and 12.")
        return
    if not (0 <= minutes <= 59):
        print("Invalid minutes. Must be between 0 and 59.")
        return

    # Convert to 24-hour hour integer
    if period == "am":
        hours24 = 0 if hours == 12 else hours
    else:  # pm
        hours24 = 12 if hours == 12 else hours + 12

    check_meal_time(hours24)


def convert_24h(time24h):
    """Parse a 24-hour time string like "HH:MM" and call check_meal_time.

    Validates hours and minutes and avoids raising exceptions on bad input.
    """
    try:
        hours_str, minutes_str = time24h.split(":")
        hours = int(hours_str)
        minutes = int(minutes_str)
    except ValueError:
        print('Invalid time format. Please use "HH:MM" (e.g. 07:30 or 18:05).')
        return

    if not (0 <= hours <= 23):
        print("Invalid hour for 24h format. Hour must be between 0 and 23.")
        return
    if not (0 <= minutes <= 59):
        print("Invalid minutes. Must be between 0 and 59.")
        return

    check_meal_time(hours)


def process(timestamp):
        match timestamp:
            case 1:
                time_str = input("Enter time in 12h format (hh:mm a.m/p.m): ").strip()
                convert_12h(time_str)
            case 2:
                time_str = input("Enter time in 24h format (HH:MM): ").strip()
                convert_24h(time_str)
            case _:
                print("Invalid option")


def check_meal_time(hours):
    """Given an integer hour in 24-hour clock, print which meal time it is.

    Uses the module-level constants. Returns None. Prints nothing if outside defined windows.
    """
    if BREAKFAST_START <= hours < BREAKFAST_END:
        print("Breakfast time")
    elif MIDDAY <= hours < LUNCH_END:
        print("Lunch time")
    elif DINNER_START <= hours < DINNER_END:
        print("Dinner time")
    else:
        print("No meal time detected for that hour.")

if __name__ == "__main__":
    main()

