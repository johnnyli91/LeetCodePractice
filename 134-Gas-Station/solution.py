class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = 0
        current_gas = 0
        current_start_position = None
        number_of_stations = len(gas)
        for i in xrange(number_of_stations):
            difference_in_gas = gas[i] - cost[i]
            total_gas += difference_in_gas
            current_gas += difference_in_gas
            if current_gas < 0:
                current_start_position = None
                current_gas = 0
            elif current_start_position == None:
                current_start_position = i
        if total_gas >= 0:
            return current_start_position
        else:
            return -1
            
            
        
        