class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = 1

        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        
        while n > 4:
            product *= 3
            n -= 3
        product *= n
        return product
        