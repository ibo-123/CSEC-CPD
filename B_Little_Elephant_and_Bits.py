n = input()
m = ""
truth = False
for i in n:
       if i == "0" and not truth:
               truth = True
       else:
              m+=i
if not truth:
        m = m[1:]
print(m)     
                