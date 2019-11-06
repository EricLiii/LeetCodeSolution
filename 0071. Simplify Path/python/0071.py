class Solution_1:
"""
Runtime: 32 ms, faster than 97.17% of Python3 online submissions for Simplify Path.
Memory Usage: 13.7 MB, less than 14.29% of Python3 online submissions for Simplify Path.
"""
    def simplifyPath(self, path: str) -> str:
        places = [p for p in path.split("/") if p!="." and p!=""]
        stack = []
        for p in places:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)