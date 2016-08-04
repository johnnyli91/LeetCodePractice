class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numbers_map = {}
        for index, num in enumerate(nums):
            try:
                if index - numbers_map[num] <= k:
                    return True
                else:
                    numbers_map[num] = index
            except KeyError:
                numbers_map[num] = index
        return False
                        
                
        