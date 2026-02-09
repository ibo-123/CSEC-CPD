for _ in range(int(input())):
        n = input()
        m =[]
        idx = 0
        while idx < len(n):
                if idx+1 < len(n):
                        if n[idx]==n[idx+1]:
                                idx+=2
                        else:
                                if not n[idx] in m:
                                           m.append(n[idx])
                                idx+=1
                else:
                        if not n[idx] in m:
                                 m.append(n[idx])
                        idx+=1
                # print(n)
        m.sort()
        print("".join(m))       