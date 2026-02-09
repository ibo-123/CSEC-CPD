n = input()
stack = []
coun = 0
idx = 0
truth = True
val = "{[(<"
dic = {")":"(" , "}":"{" , "]":"[" , ">" : "<"}
while idx < len(n) and truth:
        if  n[idx] in val:
                stack.append(n[idx])
        else:
                if not  stack:
                        truth = False
                else:
                        top = stack.pop()
                        if dic[n[idx]] != top:
                                coun+=1
        idx+=1
if truth and len(stack) == 0:
        print(coun)
else:
        print("Impossible")