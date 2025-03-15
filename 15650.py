import sys
input=sys.stdin.readline

num,length=map(int,input().rstrip().split())
stack=[]

def nm(stack,start):
    if len(stack)==length:
        print(*stack)
        return
    for i in range(start,num+1): #이전 숫자보다 작은 숫자는 제외
        stack.append(i)
        nm(stack,i+1)
        stack.pop()

nm(stack,1)