n = int(input('Enter your number'))
lst = [int(input()) for _ in range(n)]
print('เลขคู่:', [x for x in lst if x%2 == 0])
print('เลขคี่:',[x for x in lst if x%2 != 0])