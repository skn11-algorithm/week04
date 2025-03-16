import sys
n=int(sys.stdin.readline())
s=[]

for i in range(n):
    a = sys.stdin.readline().split()
# a의 0번째 인덱스로 비교한다
# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if a[0] == 'push':
        s.append(a[1])
        print(s[-1])
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

    elif a[0] == 'front':
        if len(s) == 0:
            print(-1)
        else:
            print(s[0])
    elif a[0] == 'back':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])      

    
    
