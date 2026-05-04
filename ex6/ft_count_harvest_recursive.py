def ft_count_harvest_recursive():
    day = 1
    days = int(input("Days until harvest: "))
    total_days(day, days)


def total_days(day, days):
    if day <= days:
        print(f"Day {day}")
        total_days(day + 1, days)
    else:
        print("Harvest time!")
