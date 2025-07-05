price = float(input())
if price >= 2000:
    price = price - price*15/100
elif 2000 > price >= 1000:
    price = price - price*10/100
elif 1000 > price >= 500:
    price = price - price*5/100
else:
    price = price
print(price)