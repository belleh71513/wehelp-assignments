# def twoSum(nums, target):
# # your code here
#   n = len(nums)
#   for i in range(n):
#     for j in range(i+1, n):
#       if nums[i] + nums[j] == target:
#         return i, j


def twoSum(nums, target) :
  dic = {}

  for i in range(len(nums)):
    dic[nums[i]] = i

  for j in range(len(nums)):
    goal = target - nums[j]
    if(goal in dic):
      return j, dic[goal]


result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
