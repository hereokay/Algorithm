target = int(input())

m = int(input())

broken = list(map(int, input().split()))

min_diff = abs(target-100)

for num in range(10**6):
    num_str = str(num)

    for i in range(len(num_str)):
        if int(num_str[i]) in broken:
            break

        if i==len(num_str)-1:
            min_diff = min(min_diff, abs(num-target) + len(num_str))
            if min_diff==4:
                print()

print(min_diff)
