n , m = map(int,input().split())
truth = True
arr = []
for i in range(m):
        k , l = map(int,input().split())
        arr.append((k,l))
arr.sort()
for i in range(m):
        k , l = arr[i]
        if n > k:
                n+=l
        else:
                truth = False
                break
if truth:
        print("YES")
else:
        print("NO")