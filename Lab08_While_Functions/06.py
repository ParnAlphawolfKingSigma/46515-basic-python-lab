def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

results = []

while True:
    choice = int(input())
    
    if choice == 4:
        break
    elif choice in [1, 2, 3]:
        a = int(input())
        b = int(input())
        if choice == 1:
            results.append(f"ผลลัพธ์: {add(a, b)}")
        elif choice == 2:
            results.append(f"ผลลัพธ์: {sub(a, b)}")
        else:
            results.append(f"ผลลัพธ์: {mul(a, b)}")

for r in results:
    print(r)

print("จบโปรแกรม")
