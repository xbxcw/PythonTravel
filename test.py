from time import sleep
a = 0

while True:
    a += 1
    sleep(1)
    print(a)
    if a >5:
        break
print(a+a)