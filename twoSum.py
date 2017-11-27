class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        k = 0
        for num in nums:
            k += 1
            temp_nums = nums[k:]
            if target - num in temp_nums:
                return [k-1, temp_nums.index(target-num) + k]
