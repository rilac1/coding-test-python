def bisect(left, right):
    global target
    while left <= right:
        mid = (left+right)//2
        if arr[mid] < target:
            left = mid+1
        elif arr[mid] > target:
            right = mid-1
        else: return 1
    return 0

arr = [1,2,3,4,5]
target = 2
print(bisect(0,4))