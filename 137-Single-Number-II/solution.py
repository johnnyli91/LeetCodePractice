class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numbers_map = {}
        for num in nums:
            try:
                numbers_map[num] += 1
            except KeyError:
                numbers_map[num] = 1
        for key in numbers_map:
            if numbers_map[key] == 1:
                return key
        