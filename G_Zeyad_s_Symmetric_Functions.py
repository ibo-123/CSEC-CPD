l, r = map(int, input().split())

count = r - l + 1
if l <= 0 <= r:
    count -= 1   # remove zero

print(count * 2)
