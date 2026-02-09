from collections import Counter
for _ in range(int(input())):
        n = input()
        m = input()
        s = input()
        count = Counter(n + m + s)
        var = "ABC"
        for char in var:
                if count[char] == 2:
                        print(char)