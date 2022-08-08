
class Solution:
    def isValid(self, s: str) -> bool:
        d={'(':')','[':']','{':'}'}
        stack=[]
        for i in range(len(s)):
            if len(stack):
                if d.get(stack[-1])==s[i]:
                    stack.pop(-1)
                else:
                  if s[i] in d:
                    stack.append(s[i])
                  else:
                    return False
            else:
              stack.append(s[i])
        return True if len(stack)==0 else False
