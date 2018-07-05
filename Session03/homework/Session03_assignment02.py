from random import randint

ori_tong = randint(0, 100)

tong = ori_tong

count = 0

print(ori_tong)
while count < 5:
    n = int(input("Whats your number?"))
    tong += n
    if tong < 100:
        print("Keep increasing :D")
    elif tong > 100:
        print("Decreasing!")
    else:
        print("You've won!")
        break
    count += 1

    if count == 8:
        print("You've lost!")