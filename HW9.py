class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Count = collections.Counter(S)
        totle = 0
        for j in J:
            totle += Count[j]
        return totle