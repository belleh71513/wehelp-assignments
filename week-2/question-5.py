def maxZeros(nums):
# 請用你的程式補完這個函式的區塊
  zeroLength = 0
  maxZeroLength = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      zeroLength += 1
    else:
      if zeroLength > maxZeroLength :
        maxZeroLength = zeroLength
      zeroLength = 0
  print(max(zeroLength, maxZeroLength))
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
