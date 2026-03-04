for i in range(int(input())):
        n = int(input())
        m = list(input())
        coun = m.count('1') if len(m) > 1 else 1
        for i in range( n-1):
            if not(m[i] == '1' or  m[i-1] == '1' or m[i + 1] == '1'):
                coun += 1
                m[i] = '1'
                
        print(coun)