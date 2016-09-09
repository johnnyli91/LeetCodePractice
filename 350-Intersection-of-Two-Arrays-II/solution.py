class Solution(object):
    def get_numbers_map(self, numbers):
        numbers_map = {}
        for number in numbers:
            try:
                numbers_map[number] += 1
            except KeyError:
                numbers_map[number] = 1
        return numbers_map
        
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        
        if len(nums1) > len(nums2):
            short_array = nums2
            long_array_map = self.get_numbers_map(nums1)
        else:
            short_array = nums1
            long_array_map = self.get_numbers_map(nums2)
        
        for number in short_array:
            try:
                long_array_map[number] -= 1
                if long_array_map[number] >= 0:
                    result.append(number)
            except KeyError:
                pass
        return result
        