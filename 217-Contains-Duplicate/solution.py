class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numbers_map = {}
        for num in nums:
            try:
                numbers_map[num] += 1
                return True
            except KeyError:
                numbers_map[num] = 1
        return False