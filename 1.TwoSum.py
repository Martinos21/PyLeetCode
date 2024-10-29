#def twoSum(self, nums: List[int], target: int) -> List[int]:
def twoSum(nums: list[int], target: int):
    numToIndex = {}

    for i, num in enumerate(nums):
      if target - num in numToIndex:
        return numToIndex[target - num], i
      numToIndex[num] = i