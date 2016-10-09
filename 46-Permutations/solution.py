class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        self.get_permutations(nums, [], solution)
        return solution
        
    def get_permutations(self, nums, current, solution):
        if not nums:
            solution.append(current)
        else:
            for num in nums:
                self.get_permutations([number for number in nums if number != num], current + [num], solution)
        