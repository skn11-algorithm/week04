import sys
input=sys.stdin.readline

def gcd(A,B):
    if B==0: #만약, 9자리보다 길다면, 마지막 9자리만 출력
        if A>=1000000000:
            A=A%1000000000
            print("%09d"%A)
        else:
            print(A)
        exit()
    gcd(B,A%B)

nums=[1,1]
for i in range(2):
    input()
    A=list(map(int,input().split()))
    for a in A:
        nums[i]*=a
nums.sort()
gcd(nums[1],nums[0])