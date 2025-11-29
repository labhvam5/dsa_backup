
# LINK : https://leetcode.com/problems/valid-parentheses/


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0
            
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        bracket_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        closing_brackets = ['}', ']', ')']
        for ch in s:
            if stack.is_empty():
                stack.push(ch)
            else:
                if ch in closing_brackets:
                    last_element = stack.peek()
                    opening_bracket = bracket_map[ch]
                    if opening_bracket == last_element:
                        stack.pop()
                    else:
                        stack.push(ch)
                else:
                    stack.push(ch)
        
        if stack.is_empty():
            return True
        else :
            return False
        



class Solution:
    def isValid(self, s: str) -> bool:
        # Early exit: valid strings must have even length
        if len(s) % 2 == 1:
            return False

        # Map opening -> expected closing
        expected = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            if ch in expected:
                # push the *expected* closing bracket
                stack.append(expected[ch])
            else:
                # ch is a closing bracket: must match the last expected
                if not stack or stack.pop() != ch:
                    return False

        # all expected closings must have been matched
        return not stack


