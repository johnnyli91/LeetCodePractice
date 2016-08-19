class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        available_letters = {}
        for letter in magazine:
            try:
                available_letters[letter] += 1
            except KeyError:
                available_letters[letter] = 1
        for letter in ransomNote:
            try:
                available_letters[letter] -= 1
                if available_letters[letter] < 0:
                    return False
            except KeyError:
                return False
        return True