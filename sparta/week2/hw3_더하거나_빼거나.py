numbers = [1, 1, 1, 1, 1]
target_number = 3

result = 0
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, sum, idx):
    global result
    if idx == len(array):
        if sum == target:
          result+=1
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, sum + numbers[idx], idx+1
    )
    get_count_of_ways_to_target_by_doing_plus_or_minus(
        array, target, sum - numbers[idx], idx+1
    )




get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
print(result)