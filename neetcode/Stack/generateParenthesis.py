class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from typing import List

        res = []

        def helper(curParen, opened, closed):
            if opened == closed == n:
                res.append(curParen)
                return

            if opened < n:
                helper(curParen + "(", opened + 1, closed)

            if closed < opened:
                helper(curParen + ")", opened, closed + 1)

        helper("", 0, 0)
        return res
