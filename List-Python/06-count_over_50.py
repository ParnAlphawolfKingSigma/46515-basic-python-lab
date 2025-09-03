n = int(input())
nums = [int(input()) for _ in range(n)]
count = len([x for x in nums if x > 50])
print("จำนวนที่มากกว่า 50:", count)