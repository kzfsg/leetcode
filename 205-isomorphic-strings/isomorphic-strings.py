class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashTableS = {}
        hashTableT = {}
        #maintain change counter for both
        # store mappings in the hashtable
        # then i lookup the mapping everytime i run
        # if mapping changes, then return false
        sCounter = 0
        tCounter = 0
        for i in range(len(s)):
#            if s.count(s[i]) != t.count(t[i]):
            if t[i] not in hashTableT:
                hashTableT[t[i]] = s[i]
            elif hashTableT[t[i]] != s[i]:
                return False

            if s[i] not in hashTableS:
                hashTableS[s[i]] = t[i]
            elif hashTableS[s[i]] != t[i]:
                return False
            # if hashTableS[s[i]] != t[i]: # base already mapped before // 
            #     return False
#            if len(hashTableS) != len(hashTableT): #lookup
#                return False
        return True
        # print(hashTableT)
        # print(hashTableS)
        # return True