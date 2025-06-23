Bill , TipPercent , People = input().split()
Bill = float(Bill)
TipPercent = int(TipPercent)
People = int(People)
total = (Bill * TipPercent/100) + Bill
EachPerson = total / People
print("Each person pays:", EachPerson) 