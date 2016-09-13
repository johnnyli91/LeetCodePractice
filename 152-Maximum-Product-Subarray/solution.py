class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_nums = len(nums)
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in xrange(1, length_nums):
            current_max = max_product
            max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
            min_product = min(nums[i], current_max * nums[i], min_product * nums[i])
            result = max(max_product, result)
        
        return result
