class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.values.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        temporary_queue = []
        while len(self.values) > 1:
            temporary_queue.append(self.values.pop(0))
        self.values.pop(0)
        while len(temporary_queue):
            self.values.append(temporary_queue.pop(0))
        

    def top(self):
        """
        :rtype: int
        """
        temporary_queue = []
        while len(self.values) > 1:
            temporary_queue.append(self.values.pop(0))
        top_of_stack = self.values.pop(0)
        temporary_queue.append(top_of_stack)
        while len(temporary_queue):
            self.values.append(temporary_queue.pop(0))
        return top_of_stack
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.values) <= 0
        