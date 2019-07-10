class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sort = sorted(heights)
        totle = 0
        for i,j in zip(heights,sort):
            totle += 1 if i != j else  0
        return totle