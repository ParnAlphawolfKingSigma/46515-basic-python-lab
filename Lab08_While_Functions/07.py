numbers = []

while True:
    s = input()
    if s == "end":
        break
    numbers.append(int(s))

if numbers:
    print("ค่าสูงสุด:", max(numbers))
    print("ค่าต่ำสุด:", min(numbers))