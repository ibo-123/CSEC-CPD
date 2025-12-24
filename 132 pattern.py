def find132pattern(nums):
    stack = []
    third = float('-inf')  # This will hold nums[k]

    # Traverse from right to left
    for num in reversed(nums):
        if num < third:
            return True
        while stack and stack[-1] < num:
            third = stack.pop()
        stack.append(num)

    return False
