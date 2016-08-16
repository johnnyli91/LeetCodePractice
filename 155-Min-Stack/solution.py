class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        try:
            current_min = self.min_stack[-1][1]
        except IndexError:
            current_min = x

        if current_min > x:
            current_min = x
        self.min_stack.append([x, current_min])

    def pop(self):
        """
        :rtype: void
        """
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        try:
            return self.min_stack[-1][0]
        except IndexError:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        try:
            return self.min_stack[-1][1]
        except IndexError:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()