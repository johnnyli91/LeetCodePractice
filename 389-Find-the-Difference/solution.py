class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        original_letters = {}
        modified_letters = {}
        
        for letter in s:
            try:
                original_letters[letter] += 1
            except KeyError:
                original_letters[letter] = 1
        
        for letter in t:
            try:
                modified_letters[letter] += 1
            except KeyError:
                modified_letters[letter] = 1
         
        for key in modified_letters:
            try:
                if original_letters[key] != modified_letters[key]:
                    return key
            except KeyError:
                return key
        return
