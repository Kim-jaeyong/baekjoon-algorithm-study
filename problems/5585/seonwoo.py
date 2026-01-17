# n = 1000 - int(input())
# yen_500 = n // 500
# yen_100 = n % 500 // 100
# yen_50 = n % 100 // 50
# yen_10 = n % 50 // 10
# yen_5 = n % 10 // 5
# yen_1 = n % 5
# count = yen_500 + yen_100 + yen_50 + yen_10 + yen_5 + yen_1
# print(count)

n = 1000 - int(input())

yen = [500, 100, 50, 10, 5, 1]
result = 0

for i in yen:
    result += n // i
    n = n % i

print(result)