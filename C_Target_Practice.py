import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = 0
    grid = [input().strip() for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                score += min(i, j, 9 - i, 9 - j) + 1

    print(score)