from itertools import permutations

def cal_distance(case):
    x1, x2, y1, y2 = case
    return abs(x1-x2) + abs(y1-y2)

nums = list(map(int, input().split()))
ans = 0
for case in permutations(nums, 4):
    ans = max(ans, cal_distance(case))
print(ans)

# Answer
"""
nums = list(map(int, input().split()))
nums.sort()
x = abs(nums[0] - nums[3])
y = abs(nums[1] - nums[2])

print(x+y)
"""
