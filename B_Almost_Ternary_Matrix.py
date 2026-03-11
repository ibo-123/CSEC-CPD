for i in range(int(input())):
        n , m = map(int,input().split())
        ans = []
        for j in range(n):
            cur = []
            for k in range(m):
                    if k % 2 == 0 and j % 2 == 0:
                        cur.append('1')
                    elif k % 2 == 0 and j % 2 == 1:
                        cur.append('0')
                    elif k % 2 == 1 and j % 2 == 1:
                        cur.append('1')
                    else:
                        cur.append('0')
            ans.append(' '.join(cur))
        print('\n'.join(ans))