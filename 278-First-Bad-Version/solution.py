# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        found = False
        start = 1
        end = n
        while not found:
            midpoint = (start + end) / 2
            if isBadVersion(midpoint):
                end = midpoint
            else:
                start = midpoint + 1
            if start == end:
                return start
        