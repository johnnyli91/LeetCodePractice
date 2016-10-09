class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution = []
        candidates.sort()
        self.search_solution(candidates, target, solution, [], 0)
        return solution
    
    def search_solution(self, candidates, target, solution, current_list, start_index):
        if target < 0:
            return
        elif target == 0:
            solution.append(current_list)
            return
        else:
            length_candidates = len(candidates)
            for i in xrange(start_index, length_candidates):
                self.search_solution(candidates, target - candidates[i], solution, current_list + [candidates[i]], i)
        
        