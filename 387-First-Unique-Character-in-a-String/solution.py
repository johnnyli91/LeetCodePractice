class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique_letter = None
        letter_map = {}
        for letter in s:
            try:
                letter_map[letter] += 1
            except KeyError:
                letter_map[letter] = 1
        for index, letter in enumerate(s):
            if letter_map[letter] == 1:
                return index
        return -1
