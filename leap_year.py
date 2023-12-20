_year = int(input("Enter year: "))

if _year % 4 == 0:
    if _year % 100 == 0:
        if _year % 400 == 0:
            print(f"{_year} is a leap year")
        else:
            print(f"{_year} is not a leap year")
    else:
        print(f"{_year} is a leap year")
else:
    print(f"{_year} is not a leap year")