n = int(input())
fib = 1
new = [1 , 1]
for i in range(1,n + 1 ):
        new.append(new[-1] + new[-2])
# print(new)
m = ""
for i in range(1 , n + 1):
        if i in new:
            m+="O"
        else:
                m+="o"    
print(m)