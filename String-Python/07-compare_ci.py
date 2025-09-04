string=input()
n1=string[0].lower()
n2=string[1].lower()
if(n1 > n2):
    print("A comes after B")
elif(n1 < n2):
    print("A comes before B")
else:
    print("A equals to B")