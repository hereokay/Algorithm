
str = input()

while True:
    if len(str) >= 10:
        print(str[:10])
        str = str[10:]
    else:
        if len(str)==0:
            break
        print(str)
        break
