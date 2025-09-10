def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

nums = []
while True:
    x = int(input())
    if x == 0:
        break
    nums.append(x)

for n in nums:
    print(f"{n} prime" if is_prime(n) else f"{n} not prime")
