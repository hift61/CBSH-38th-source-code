import sys

S = input().rstrip()

tmp = []
for s in S:
    if s in ['(', '[']:
        tmp.append(s)
    else:
        if s == ')':
            if not tmp:
                print("NO")
                sys.exit()
            elif tmp[-1] == '(':
                tmp.pop(-1)
            else:
                print("NO")
                sys.exit()
        if s == ']':
            if not tmp:
                print("NO")
                sys.exit()
            elif tmp[-1] == '[':
                tmp.pop(-1)
            else:
                print("NO")
                sys.exit()

if not tmp:
    print("YES")
else:
    print("NO")