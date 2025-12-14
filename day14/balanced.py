#balanced parenthises
def balanced_parenth(exp):
    stack=[]
    pairs={'[':']','{':'}','(':')'}
    for ch in exp:
        if ch in pairs:
            stack.append(ch)
        elif ch in pairs.values():
            if not stack:
                return False
            if pairs[stack.pop()]!=ch:
                return False
    return len(stack)==0
exp=input()
res=balanced_parenth(exp)
print("expression:",exp)
print("result:",res)