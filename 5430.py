import sys
input=sys.stdin.readline

N=int(input())
flag=True
for _ in range(N):
    AC=input()
    d=int(input())
    arr=input().strip()[1:-1]
    arr=arr.split(',') if arr else []
    arr=[int(a) for a in arr]

    for ac in AC:
        if ac=="R":
            arr.reverse()
        elif ac=='D':
            if d==0:
                flag=False
                print("error")
            else:
                if len(arr)==0 or not arr:
                    flag=False
                    print("error")
                else:
                    flag=True
                    arr=arr[1:]
    if flag:
        print(arr)
