
def average(nums):
    return round(sum(nums) / len(nums))

def median(nums):
    return nums[len(nums) // 2]

def nums_range(nums):
    return nums[-1] - nums[0]

def mod(nums):
    dic = {}
    for i in range(len(nums)):
        n = nums[i]
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1

    most = 0
    eq_list = []
    for k, v in dic.items():
        if v > most: # 더 큰 값 찾았을 때
            most = v
            eq_list.clear()
            eq_list.append(k)
        elif v == most: # 현재 최빈값과 같을 때
            eq_list.append(k)



    if len(eq_list) >= 2:
        eq_list = sorted(eq_list)
        return eq_list[1]
    return eq_list[0]



n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

nums = sorted(nums)

avg = average(nums)
med = median(nums)
mod = mod(nums)
range = nums_range(nums)

print(avg)
print(med)
print(mod)
print(range)


