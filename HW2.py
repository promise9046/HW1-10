class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        string = text.split()
        result = []
        L = len(string)
        for i in range(L - 2):
            F, S, time = string[i], string[i + 1], string[i + 2]
            if F == first and S == second:
                result.append(time)
        return result