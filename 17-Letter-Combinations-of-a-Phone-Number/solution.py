class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        solution = []
        self.generate_letters(digits, solution, [])
        return [''.join(list_solution) for list_solution in solution]
        
    def generate_letters(self, digits, solution, current_list):
        NUMBER_LETTER_MAP = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }

        try:
            first_digit = digits[0]
        except IndexError:
            if current_list:
                solution.append(current_list)
            return
        
        first_digit_map = NUMBER_LETTER_MAP[first_digit]
        length_digit_map = len(first_digit_map)
        for i in xrange(length_digit_map):
            self.generate_letters(digits[1:], solution, current_list + [first_digit_map[i]])
