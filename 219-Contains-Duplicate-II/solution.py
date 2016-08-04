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
                numbers_map[num].append(index)
            except KeyError:
                numbers_map[num] = [index]
        for key in numbers_map:
            number_of_indices = len(numbers_map[key])
            if number_of_indices > 1:
                index_pointer = number_of_indices - 1
                prev_index_pointer = index_pointer - 1
                while index_pointer > 0:
                    difference = numbers_map[key][index_pointer] - numbers_map[key][prev_index_pointer]
                    if difference <= k:
                        return True
                    else:
                        index_pointer -= 1
                        prev_index_pointer = index_pointer - 1
        return False
                        
                
        