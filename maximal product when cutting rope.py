'''
Given a rope with integer-length n, how to cut the rope into m integer-length parts with length p[0], p[1], ..., p[m-1],
in order to get the maximal product of p[0] * p[1] *...* p[m-1]?
 m is determined by you and must be greater than 0(at least one cut must be made).

'''
from functools import lru_cache
class Solution:

    def cutRope(self, n):
        dp = dict()
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = 0
            for j in range(1, i):
                dp[i] = max(dp[i], j * max(i - j, dp[i - j]))
        return dp[n]

    '''
    @lru_cache()
    def cutRope(self, n):
        if n <= 1:
            return 0
        maxProduct = 0
        for i in range(1, n):
            maxProduct = max(maxProduct, i * max(n - i, self.cutRope(n - i)))
        return maxProduct
    '''

if __name__  == '__main__':
    o = Solution()
    print(2, o.cutRope(2))
    print(3, o.cutRope(3))
    print(4, o.cutRope(4))
    print(5, o.cutRope(5))
    print(6, o.cutRope(6))
    print(7, o.cutRope(7))
    print(8, o.cutRope(8))
    print(9, o.cutRope(9))
    print(10, o.cutRope(10))
    print(11, o.cutRope(11))

'''
result:
2 1
3 2
4 4
5 6
6 9
7 12
8 18
9 27
10 36
11 54
'''