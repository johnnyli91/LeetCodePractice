class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        checked_numbers = []
        current_number = n
        while True:
            checked_numbers.append(current_number)
            sum = self.calculate_sum_squares(current_number)
            if sum == 1:
                return True
            elif sum in checked_numbers:
                return False
            else:
                current_number = sum
        
    def calculate_sum_squares(self, number):
        total = 0
        string_number = str(number)
        for num in string_number:
            total += int(num) * int(num)
        return total