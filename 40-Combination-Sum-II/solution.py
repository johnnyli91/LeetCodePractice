class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution = []
        candidates.sort()
        self.search_solution(candidates, target, 0, solution, [])
        return solution
        
    def search_solution(self, candidates, target, start_index, solution, current_list):
        if target < 0:
            return
        elif target == 0:
            if current_list not in solution:
                solution.append(current_list)
            return
        else:
            length_candidates = len(candidates)
            for i in xrange(start_index, length_candidates):
                self.search_solution(candidates, target - candidates[i], i + 1, solution, current_list + [candidates[i]])
        