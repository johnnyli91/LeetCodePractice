class Solution(object):
    def wordPattern(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        split_string = string.split()
        letter_to_word_map = {}
        if len(split_string) != len(pattern):
            return False

        for index, letter in enumerate(pattern):
            try:
                if letter_to_word_map[letter] != split_string[index]:
                    return False
            except KeyError:
                if split_string[index] in letter_to_word_map.values():
                    return False
                letter_to_word_map[letter] = split_string[index]
        
        return True
                    