class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(numRows):
            current_row = []
            try:
                last_row = result[-1]
            except IndexError:
                last_row = []
            for index, number in enumerate(last_row):
                if index > 0:
                    current_row.append(number + last_row[index - 1])
                else:
                    current_row.append(number)
            current_row.append(1)
            result.append(current_row)
        return result