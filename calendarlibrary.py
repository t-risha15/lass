import calendar

year =int(input("Enter year:"))

if calendar.isleap(year):
    print("This is a leap year")
else:
    print("This is not a leap year")