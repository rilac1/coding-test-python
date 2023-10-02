N = int(input())
M = int(input())
nums = list(map(int, input().split()))

nums.sort()

left, right = 0, N-1
ans = 0
while left < right:
    result = nums[left] + nums[right]
    if result > M:
        right -= 1
    elif result < M:
        left += 1
    else:
        ans += 1
        left += 1
        right -= 1
print(ans)
