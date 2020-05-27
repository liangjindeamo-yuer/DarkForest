i = 1
b = 9900
c = 101
while True:
    a = b * i - c * int(b * i / c)
    if a == 1:
        print(i)
        break
    else:
        i = i + 1
