
nums = list(range(1,11))
more_nums = list(range(12,21))
all_nums = [*nums, *more_nums]
print(all_nums)
print(all_nums.remove(all_nums[5]))
