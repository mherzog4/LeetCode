class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        
        for character in s:
            if character in closeToOpen:
                if stack and stack[-1] == closeToOpen[character]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(character)
        return True if not stack else False
                
            
                
        