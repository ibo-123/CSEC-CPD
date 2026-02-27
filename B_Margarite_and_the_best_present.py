for i in range(int(input())):
    l , r = map(int, input().split())
    if l % 2 == 0:
            first = l // 2
    else:
           first = -(l + 1) // 2
    if r % 2 == 0:
            second = r // 2
    else:           second = -(r + 1) // 2
    print(second - (first - 1))