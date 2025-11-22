from typing import List

import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evals = ['+', '-', '*','/']
        stack = []
        evals_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for token in tokens:
            if not token in evals:
                stack.append(token)
            else:
                pop_1 = int(stack.pop())
                pop_2 = int(stack.pop())

                res = int(evals_map[token](pop_2, pop_1))

                stack.append(res)

        return stack[-1]
        