a = int(input())

lm = 1000 - a

b = (lm // 500) + (lm % 500 // 100) + (lm % 100 // 50) + (lm % 50 // 10) + (lm % 10 // 5) + lm % 5

print(b)