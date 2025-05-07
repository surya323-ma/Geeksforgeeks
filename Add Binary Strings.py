Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.
#User function Template for python3
class Solution:
    def addBinary(self, s1, s2):
        s1=s1.lstrip('0')
        s2=s2.lstrip('0')
        if not s1:
            s1='0'
        if not s2:
            s2='0'
        result =[]
        carry=0
        max_len=max(len(s1),len(s2))
        s1=s1.zfill(max_len)
        s2=s2.zfill(max_len)
        for i in range(max_len -1,-1,-1):
            total=int(s1[i])+int(s2[i])+carry
            carry=total//2
            result.append(str(total%2))
        if carry:
            result.append('1')
        result.reverse()
        return''.join(result)
        # code here
