class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        letter_map = {}
        converted_letters = {}
        for index, letter in enumerate(s):
            try:
                if letter_map[letter] != t[index]:
                    return False
            except KeyError:
                try:
                    if converted_letters[t[index]] == True:
                        return False
                except KeyError:
                    letter_map[letter] = t[index]
                    converted_letters[t[index]] = True
        return True
        