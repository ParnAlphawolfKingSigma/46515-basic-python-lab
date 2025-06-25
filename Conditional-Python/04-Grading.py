point = int(input())
midterm = int(input())
final = int(input())

if point<0 or point>30:
    print("Enter again")
elif midterm<0 or midterm>30:
    print("Enter again")
elif final<0 or final>40:
    print("Enter again")
else:
    if point+midterm+final >= 80:
        print("A")
    elif 75<=point+midterm+final <=79:
        print("B+")
    elif 70<=point+midterm+final <=74:
        print("B")
    elif 65<=point+midterm+final <=69:
        print("C+")
    elif 60<=point+midterm+final <=64:
        print("C")
    elif 55<=point+midterm+final <=59:
        print("D+")
    elif 50<=point+midterm+final <=54:
        print("D")
    else:
        print("F")