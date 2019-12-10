class Solution:
    def minSteps(self, n):
        """
        we use C represent copying and P represent pasting.And final results could be divided into groups like [CPP],[CPPP].And their length are g_1,g_2,...,g_n respectively.
        So the final number of 'A' is equal to g_1*g_2*g_3...g_n.Suppose n is decomposable and n=p*q.We can make a conclusion that we need (p-1) pasting and (q-1) pasting.
        Until factor 1 occur in factors, we finish the work.Based on the above assumption,given n,we exactly want n=g_1*g_2*g_3...g_k.As a result, the sequence can be divided into k groups and minimum steps = g_1+g_2+g_3+g_4+...+g_k.
        :type n: int
        :rtype: int
        :linked url: https://leetcode.com/problems/2-keys-keyboard/
        """
        results = 0
        factor=2
        while n > 1:
            while n % factor == 0:
                results += factor
                n/=factor
            factor+=1
        return results