year=int(input())
if year%4 == 0 and year%100 != 0 and year%400:
    year = "Leap Year"
else:
    year = "Not a Leap Year"

print(year)
