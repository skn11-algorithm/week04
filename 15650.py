import sys
input=sys.stdin.readline

num,length=map(int,input().rstrip().split())
stack=[]
ck=[False]*(num+1)
def nm(stack):
    if len(stack)==length:
        print(*stack)
        return
    for i in range(1,num+1):
        if not ck[i]:
            stack.append(i)
            ck[i]=True
            nm(stack)
            stack.pop()
            ck[i]=False

nm(stack)