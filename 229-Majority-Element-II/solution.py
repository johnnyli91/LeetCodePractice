class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        number_limit = len(nums) / 3
        all_nums = {}
        result = []
        for num in nums:
            try:
                if all_nums[num] >= 0:
                    all_nums[num] += 1
            except KeyError:
                all_nums[num] = 1

            if all_nums[num] > number_limit:
                result.append(num)
                all_nums[num] = -1
        return result
        