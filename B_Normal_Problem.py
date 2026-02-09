for  i in range(int(input())):
        n = input()
        m = reversed(n)
        m = list(m)
        for j in range(len(n)):
            if m[j] == "p":
                    m[j] = "q"
            elif m[j] == "q":
                    m[j] = "p"
        print("".join(m))