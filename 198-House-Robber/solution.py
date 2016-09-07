class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        previous_total = 0
        total = 0
        for num in nums:
            current_total = total
            total = max(previous_total + num, current_total)
            previous_total = current_total
        return total
        