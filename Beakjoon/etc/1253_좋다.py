# 두 포인터
N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N):
    left = 0
    right = N - 1

    while left < right:
        result = A[left] + A[right]
        if i == left or result < A[i]:
            left += 1
        elif i == right or result > A[i]:
            right -= 1
        else:
            ans += 1
            break
print(ans)
