def eval_postfix(exp):
    stack=[]
    for ch in  exp:
        if ch.isdigit():
            stack.append(int(ch))
        elif ch in '+-*/':
            if len(stack)<2:
                raise ValueError("invalid Expression")
            val1=stack.pop()
            val2=stack.pop()
            if ch=='+':
                r=val2+val1
            elif ch=='-':
                r=val2-val1
            elif ch=='*':
                r=val2*val1
            elif ch=='/':
                r=val2/val1
            stack.append(r)
    return stack[0] if stack else 0
exp="231*+9-"
print(eval_postfix(exp))