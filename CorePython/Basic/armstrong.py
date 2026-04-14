number = 153
n = number
sum = 0
while n > 0:
    r = n % 10
    sum = sum + r * r * r
    n = n // 10
if sum == number:
    print("this is armstrong", sum)
else:
    print("not arms ")
