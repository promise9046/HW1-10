class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in A:
            if i % 2 == 0:
                result.insert(0,i)
            else:
                result.append(i)
        return result