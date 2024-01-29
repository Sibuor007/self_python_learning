# function to check for leap year
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# function to get the days of months
def days_in_month(year, month):
    # create a list of days per month that will be accessed through index
    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # check for validity of months
    if month < 1 or month > 12:
        return "Invalid month"
    # handle feb on leap year
    if leap_year(year) and month == 2:
        return 29
    # return normal unaffected days
    else:
        return days_list[month - 1]


# take input from user
year = int(input("Enter year: \n"))
month = int(input("Enter month: \n"))
# print the days from called function
print(days_in_month(year, month))
