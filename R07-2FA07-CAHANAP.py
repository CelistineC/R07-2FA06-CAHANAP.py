from datetime import date

title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

d = date(year, month, day)

print("\nFormatted Output:")
print("Event:", title.upper())
print("Date:", d.strftime("%B %d, %Y"))
print("Year:", d.year)
print("Month:", d.strftime("%B"))
print("Day:", d.day)
print("Weekday:", d.strftime("%A"))
