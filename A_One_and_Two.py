for i in range(int(input())):
        n = int(input())
        arr = list(map(int , input().split()))
        if len(set(arr)) == 1 and arr[0] == 1:
                print(1)
        else:
                two = arr.count(2)
                if two % 2 == 0:
                        must = two // 2
                        idx = 0
                        while must > 0:
                                if arr[idx] == 2:
                                        must -= 1
                                idx += 1
                        print(idx+1)
                else:
                        print(-1)