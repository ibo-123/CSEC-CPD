def digit_sum(n):
    return sum(int(d) for d in str(n))

t = int(input())
for _ in range(t):
    x = int(input())
    count = 0
    
    for y in range(x, x + 91):   # check possible y values
        if y - digit_sum(y) == x:
            count += 1
    
    print(count)
