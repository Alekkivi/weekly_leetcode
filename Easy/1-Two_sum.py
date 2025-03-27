
# Initial version, not optimized
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]


    Rational: Not a great solution as O(n^2) time complexity due to nested for-loops.
    """
    
    for i, a in enumerate(nums):
        for b in range(i + 1, len(nums)):
            if a + nums[b] == target: return [i, b]
    


def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    nums_map = {}

    for i, num in enumerate(nums):

        missing_num = target - num

        if missing_num in nums_map:
            return [nums_map[missing_num], i]
        else:
            nums_map[num] = i
    return []



nums = [3,3]
target = 6
print(twoSum2(nums, target))