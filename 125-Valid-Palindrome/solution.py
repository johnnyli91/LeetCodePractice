import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        excluded_values = list(string.punctuation)
        excluded_values.append(" ")
        cleaned_string_value = [letter for letter in s if letter not in excluded_values]
        cleaned_string = "".join(cleaned_string_value).lower()
        return cleaned_string == cleaned_string[::-1]
        