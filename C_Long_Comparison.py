for i in range(int(input())):
        n , m = map(int,input().split())
        k , l = map(int,input().split())
        ans1 = len(str(n))+m
        ans2 = len(str(k))+l
        if ans1 > ans2:
                print(">")
        elif ans1 < ans2:
                print("<")
        else:
                max_ = max(len(str(n)) ,len(str(k)))
                if len(str(n)) < max_ :
                        n=str(n)+("0"*(max_-len(str(n))))
                elif len(str(k)) < max_:
                        k =str(k)+"0"*(max_-len(str(k)))
                if int(n) > int(k):
                        print(">")
                elif int(n) < int(k):
                        print("<")
                else:
                        print("=")
                # print(n,k,max_)