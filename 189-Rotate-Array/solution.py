class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        length_nums = len(nums)
        if k > length_nums:
            positions_moved = k % length_nums
        else:
            positions_moved = k
        for i in xrange(positions_moved):
            number = nums.pop()
            nums.insert(0, number)
        return
        