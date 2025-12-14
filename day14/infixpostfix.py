def in_to_post(infix):
    precd={'+':1,'-':1,'*':2,'/':2,'^':3}
    stack = []
    postfix = ''
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precd.get(char, 0) <= precd.get(stack[-1], 0):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix
exp="a+b*(c-d)"
print(in_to_post(exp))