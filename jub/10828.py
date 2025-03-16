import sys
n=int(sys.stdin.readline())
s=[]

for i in range(n):
    a = sys.stdin.readline().split()
# a의 0번째 인덱스로 비교한다
# push / pop
# size / empty
# top

    if a[0] == 'push':
        s.append(a[1])
    elif a[0] == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())

    elif a[0] == 'size':
        print(len(s))
    elif a[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)

    elif a[0] == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])


    
    
