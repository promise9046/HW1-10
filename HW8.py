class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        A_edge = len(A)
        B_edge = len(A[0])
        result = [[0] * B_edge for _ in range(A_edge)]
        for i in range(A_edge):
            for j in range(B_edge):
                result[i][j] = 1 - A[i][B_edge - 1 - j]
        return result