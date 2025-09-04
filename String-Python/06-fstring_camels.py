string = input().strip()
i = 0
n1 = ""
l1 = ""

while i < len(string):
    if string[i].isdigit() or string[i] == ".":
        n1 += string[i]
    elif string[i].isalpha():
        l1 += string[i]
    i += 1

if len(n1) >= 2:
    print(f"In {n1[0]} years I have spotted {n1[1:]} {l1}.")