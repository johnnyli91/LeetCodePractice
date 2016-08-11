class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = list(nums)
        self.sum_of_nums = nums
        
        length_nums = len(self.nums)
        for index in xrange(1, length_nums):
            self.sum_of_nums[index] += self.sum_of_nums[index - 1]
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum_of_nums[j] - self.sum_of_nums[i] + self.nums [i]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)