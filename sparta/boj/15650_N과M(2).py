

n, m = map(int, input().split())

def solve(nums, l):
    if l == m:
        for num in nums:
            print(num, end=' ')
        print()
        return
    for i in range(1, n+1):
        if l > 0:
            if i > nums[l-1]:
                nums[l] = i
                solve(nums, l+1)
        else:
            nums[l] = i
            solve(nums, l + 1)

nums = [0] * m
solve(nums, 0)