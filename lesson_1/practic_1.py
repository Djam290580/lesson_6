i = 0
n = True
while True:
    i += 1
    if i >= 10:
        n = False
    if i % 2 == 0:
        continue
    print(i)