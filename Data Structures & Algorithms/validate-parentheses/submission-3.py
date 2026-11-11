class Solution:
    def isValid(self, s: str) -> bool:
        res={}
        openStack = []
        closeStack = []
        for i in s:
            if i in ["[", "{", "("]:
                openStack.append(i)
            else:
                if openStack:
                    match(openStack[-1]):
                        case '(':
                            if i != ')':
                                return False
                            else:
                                openStack.pop()
                        case '{':
                            if i != '}':
                                return False
                            else:
                                openStack.pop()
                        case '[':
                            if i != ']':
                                return False
                            else:
                                openStack.pop()
                else:
                    return False                                         

        return len(openStack) == 0

        