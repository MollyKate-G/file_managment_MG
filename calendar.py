def calendar():

    month = int(input("Enter a month, (Ex:02): "))
    year = int(input("Enter a year, (Ex:1995): "))
    def is_leap_year(year):
        return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))

    def get_days_in_month(month, year):
        if month == 2:
            if is_leap_year(year):
                return 29
        else: 
            return 28

        short_months = [4, 6, 9, 11]

        if month in short_months:
            return 30
        else:
            return 31

    def day_of_week(month, year):
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if month < 3: 
            year -= 1
        return (year + int(year/4) - int(year/100) + int(year/400) + t[month - 1] + 1) % 7

    def print_month_calendar(month, year):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December',]
        day_list = ["S", "M", "T", "W", "T", "F", "S"]

        days = get_days_in_month(month, year)
        start_day_of_week = day_of_week(month, year)

        title = f'{months[month -1]} {year}'
        print(f'{title:^28} \n')

        for day in day_list:
            print(f'{str(day):>3} ', end = ' ')

        print('\n')

        current_day_of_week = 0

        while current_day_of_week < start_day_of_week:
            print("{:3} ".format(' '), end = ' ')
            current_day_of_week = (current_day_of_week + 1) % 7

        for d in range(1, days + 1):
            print("{:3} ".format(d), end =' ')

            current_day_of_week = (current_day_of_week + 1) % 7

            if current_day_of_week == 0:
                print('\n')

        print ()

    print_month_calendar(month, year)
    return