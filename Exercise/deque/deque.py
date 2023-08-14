from collections import deque

dq = deque()

def brackets(line):
    for i in line:
        if i == '(':
            dq.append('(')
        else:
            if not dq or dq.pop() != '(':
                return False
    
    return len(dq) == 0

print(brackets("(()())"))