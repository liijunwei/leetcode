# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s:
            return None
        if s.find('[') == -1:
            return NestedInteger(int(s))

        last = None
        n = 0; pos = 1; is_integer = 0
        stack = [NestedInteger()]
        i = 1; l = len(s)
        while i < l:
            if s[i] == '-':
                pos = -1
            elif s[i].isdigit():
                is_integer = 1
                n = n * 10 + int(s[i])
            elif s[i] == ',' and is_integer:
                stack[-1].add(NestedInteger(n*pos))
                n = 0; is_integer = 0; pos = 1
            elif s[i] == ']':
                if is_integer:
                    stack[-1].add(NestedInteger(n*pos))
                    n = 0; is_integer = 0; pos = 1
                last = stack.pop()
                if stack:
                    stack[-1].add(last)
            elif s[i] == '[':
                stack.append(NestedInteger())
            i += 1
        return last
