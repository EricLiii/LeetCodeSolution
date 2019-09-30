class Solution_1:
"""
Runtime: 40 ms, faster than 75.90% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Restore IP Addresses.
"""
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                    
class Solution_2:
"""
Runtime: 36 ms, faster than 92.12% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Restore IP Addresses.

Idea:
用迭代而不是递归，非常快!
link: https://leetcode.com/problems/restore-ip-addresses/discuss/30972/WHO-CAN-BEAT-THIS-CODE
"""
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    d = len(s)-a-b-c
                    if 0 < d <=3: # and a+b+c+d == len(s):
                        A, B, C, D = int(s[:a]), int(s[a:a+b]), int(s[a+b:a+b+c]), int(s[a+b+c:])
                        if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                            tmp = str(A) + "." + str(B) + "." + str(C) + "." + str(D)
                            if len(tmp) == len(s) + 3:
                                res.append(tmp)
        return res
                     