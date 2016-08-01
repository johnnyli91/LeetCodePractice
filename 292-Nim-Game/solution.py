class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        MIN_LOSE_VALUE = 4

        return n % MIN_LOSE_VALUE != 0