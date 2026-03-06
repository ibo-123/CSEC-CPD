for j in range(int(input())):
        n , k = map(int, input().split())
        store = []
        for i in range(n):
                l , r , real = map(int, input().split())
                store.append((l , r , real))
        store[2].sort()
                