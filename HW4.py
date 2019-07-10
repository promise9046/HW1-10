class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        result= ''
        count=0
        for s in S:
            if(count==0 and s=='('):
                count-=1
                continue
            elif(count==-1 and s==')'):
                count+=1
                continue
            else:
                result+=s
            if(s=='('):
                count-=1
            else:
                count+=1
        return result