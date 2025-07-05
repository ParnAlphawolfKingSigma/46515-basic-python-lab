first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number >= second_number:
    maximum = first_number
else:
    maximum = second_number
if maximum >= third_number:
    maximum = maximum
else:
    maximum = third_number

print(maximum)