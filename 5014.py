

end, target, current, up, down = map(int,input().split())

diff = abs(up-down)

target = (target-1) % diff
target += 1


