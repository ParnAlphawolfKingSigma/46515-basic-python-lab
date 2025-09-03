n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    if 10 <= num <= 50:
        numbers.append(num)

print("ค่าที่อยู่ในช่วง 10-50:", numbers)