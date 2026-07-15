class Solution:
    def isValid(self, s: str) -> bool:
        lib = {
            '(': ')', 
            '{': '}', 
            '[':']'
        }
        stack = []#holds all the openers
        for c in s:
            if c in lib.keys():#if it is an opener
                stack.append(c)
            else:
                if not stack:#if the stack is empty but you still have a closer, then its false
                    return False
                elif lib[stack.pop()] == c:#does the next character match the corresponding closer on the stack
                    continue
                else:
                    return False

        return not stack#if the has something inside (true), then return false because its add then
