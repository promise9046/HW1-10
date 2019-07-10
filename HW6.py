class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        mini = 0
        maxm = len(S)
        result = []
        for i in S:
            if i == 'I':
                result.append(mini)
                mini += 1
            else:
                result.append(maxm)
                maxm -= 1
        result.append(mini)
        return result