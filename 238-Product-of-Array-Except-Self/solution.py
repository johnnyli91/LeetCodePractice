class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current_product_first_pass = 1
        current_product_second_pass = 1
        length_nums = len(nums)
        result = []
        for num in nums:
            result.append(current_product_first_pass)
            current_product_first_pass *= num

        for i in xrange(length_nums - 1, -1, -1):
            result[i] *= current_product_second_pass
            current_product_second_pass *= nums[i]
        return result
            