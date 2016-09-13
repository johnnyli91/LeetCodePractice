class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = len(nums) / 2
        all_nums = {}
        for num in nums:
            try:
                all_nums[num] += 1
            except KeyError:
                all_nums[num] = 1
            
            if all_nums[num] > majority:
                return num
        return
        