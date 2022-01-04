def maxProduct(nums):
# 請用你的程式補完這個函式的區塊
  num1, num2 = findMaxNums(nums)
  num3, num4 = findMinNums(nums)

  result = max(num1*num2, num3*num4)
  print(result)


def findMaxNums(nums) :
  maxNums = max(nums[0], nums[1])
  secMax = min(nums[0], nums[1])
  n = len(nums)
  for i in range(2, n):
    if nums[i] > maxNums:
      secMax = maxNums
      maxNums = nums[i]
    elif nums[i] > secMax:
      secMax = nums[i]
  return maxNums, secMax


def findMinNums(nums) :
  minNums = min(nums[0], nums[1])
  secMin = max(nums[0], nums[1])
  n = len(nums)
  for i in range(2, n):
    if nums[i] < minNums:
      secMin = minNums
      minNums = nums[i]
    elif nums[i] < secMin:
      secMin = nums[i]
  return minNums, secMin


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2
