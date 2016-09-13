class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length_of_nums = len(nums)
        counter = 0
        pointer = 0
        while counter < length_of_nums:
            if nums[pointer] == 0:
                nums.pop(pointer)
                nums.insert(0, 0)
                pointer += 1
            elif nums[pointer] == 2:
                nums.pop(pointer)
                nums.insert(length_of_nums - 1, 2)
            else:
                pointer += 1
            counter += 1