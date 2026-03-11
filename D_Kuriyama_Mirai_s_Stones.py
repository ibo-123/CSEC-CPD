n = int(input())
arr = list(map(int, input().split()))
prefix_one = [0] * (len(arr) + 1)
prefix_two = [0] * (len(arr) + 1)
new_arr = sorted(arr)
for i in range(1, len(arr) + 1):
        prefix_one[i] = prefix_one[i - 1] + new_arr[i - 1]
        prefix_two[i] = prefix_two[i - 1] + arr[i - 1]
for i in range(int(input())):
        t, l , r = map(int, input().split())
        if t == 1:
                print(prefix_two[r] - prefix_two[l - 1])
        else:
                print(prefix_one[r] - prefix_one[l - 1])