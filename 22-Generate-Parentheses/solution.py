class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solution = []
        self.find_solution(solution, n, [], 0)
        return ["".join(list_solution) for list_solution in solution]
        
    def find_solution(self, solution, n, current_list, number_unmatched_parenthesis):
        if number_unmatched_parenthesis < 0:
            return
        elif number_unmatched_parenthesis > n:
            return
        elif n == 0 and number_unmatched_parenthesis == 0:
            solution.append(current_list)
            return
        else:
            self.find_solution(solution, n, current_list + ["("], number_unmatched_parenthesis + 1)
            self.find_solution(solution, n - 1, current_list + [")"], number_unmatched_parenthesis - 1)
        