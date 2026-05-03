def ft_harvest_total():
    days = 1
    total = 0
    while days <= 3:
        harvest = int(input(f'Day {days} harvest: '))
        total += harvest
        days += 1
    print('Total harvest:', total)


ft_harvest_total()
