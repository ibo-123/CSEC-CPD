# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     score = 0
#     grid = [input().strip() for _ in range(10)]

#     for i in range(10):
#         for j in range(10):
#             if grid[i][j] == 'X':
#                 score += min(i, j, 9 - i, 9 - j) + 1

#     print(score)
def backtrack(i, current, nums):
    if i == len(nums):
        print(current)
        return

    # take nums[i]
    print(current)
    current.append(nums[i])
    backtrack(i+1, current, nums)

    # don't take nums[i] (undo)
    current.pop()
    backtrack(i+1, current, nums)

backtrack(0, [], [1,2,3])