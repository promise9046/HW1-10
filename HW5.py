class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A) / 2
        count = collections.Counter(A)
        for m, n in count.items():
            if n == N:
                return m
