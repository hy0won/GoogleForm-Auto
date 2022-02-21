dartResult = '1S2D*3T'
stack = []
dartResult = dartResult.replace("10", "n")
bonus = {'S':1, 'D':2, 'T':3}

for i in dartResult:
    if i.isdigit() or i=="n":
        stack.append(10 if i=="n" else int(i))
    elif i in ('S', 'D', 'T'):
        num = stack.pop()
        stack.append(num**bonus[i])
    elif i=='#':
        stack[-1]*=-1
    elif i=='*':
        num = stack.pop()
        if len(stack):
            stack[-1]*=2
        stack.append(2*num)
print(sum(stack))

print(bonus['D'])