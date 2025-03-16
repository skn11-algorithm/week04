import sys
input=sys.stdin.readline

N=int(input())
flag=True
for _ in range(N):
    AC=input()
    d=int(input())
    arr=list(((input().lstrip('[')).rstrip(']')).rstrip().split(','))
    for ac in AC:
        flag=True
        if ac=="R":
            arr.reverse()
        elif ac=='D':
            if d==0:
                flag=False
                print("error")
            else:
                if not arr:
                    flag=False
                    print("error")
                else:
                    arr=arr[1:]
    if flag:
        print(arr)
