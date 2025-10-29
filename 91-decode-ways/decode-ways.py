# dp -> dp[i] will represent the number of ways to decode the substring from i to the end
# base case: dp[n] = 1, or if i encounter a 0
# state trasitions -> at each position i can either decode one digit or decode two digits, so this is either [i+1] or [i+2]

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        n = len(s)

        dp = [0] * (n+1)

        dp[n] = 1
 
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue

            dp[i] = dp[i+1]

            if i + 1 < n:
                two_digit = int(s[i:i+2])
                if 10 <= two_digit <= 26:
                    dp[i] += dp[i+2]

        return dp[0]
        