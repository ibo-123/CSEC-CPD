

# for _ in range(int(input())):
#     n = int(input())
#     g = [list(map(int,input().split())) for _ in range(n)]

#     p = [0]*(2*n+1)

#     for i in range(n):
#         for j in range(n):
#             p[i+j+2] = g[i][j]

#     used = set(p[2:])
#     for x in range(1,2*n+1):
#         if x not in used:
#             p[1] = x
#             break

#     print(*p[1:])



# for _ in range(int(input())):
#     n = int(input())
#     g = [list(map(int,input().split())) for _ in range(n)]

#     p = [0]*(2*n+1)

#     for i in range(n):
#         p[i+2] = g[i][0]

#     for j in range(1,n):
#         p[n+j+1] = g[n-1][j]

#     p[1] = list(set(range(1,2*n+1)) - set(p[2:]))[0]

#     print(*p[1:])










for  i in range(int(input())):
        n = int(input())
        new_arr = [0]*(2*n+1)
        for k in range(n):
                arr = list(map(int, input().split()))
                for j in range(n):
                        if arr[j] not in new_arr:
                                new_arr[k+j+1] = arr[j]
        new_set = set(new_arr)
        idx = 1
        for i in range(1,2*n+1):
                if i not in new_set:
                        idx = i
                        break
        new_arr[0] = idx
        print(*new_arr[:-1])