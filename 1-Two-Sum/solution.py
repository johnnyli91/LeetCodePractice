class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_length = len(nums)
        all_nums = {}
        for i in xrange(num_length):
            needed_number = target - nums[i]
            try:
                j = all_nums[needed_number]
                return [j, i]
            except KeyError:
                all_nums[nums[i]] = i
