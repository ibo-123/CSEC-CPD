for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        new_arr = [arr[0]]
        for j in arr[1:]:
                if new_arr[-1] != 1:
                    new_arr.append(1)
                new_arr.append(j)
        print(len(new_arr))
        print(*new_arr)