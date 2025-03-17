# 지난주차에 풀었던것!!
ir= input()
stack=[]
cnt = 0

for i in range(len(ir)):
    if ir[i] == "(":
        stack.append("(")
    else :
        if ir[i-1]=="(":
            stack.pop()
            cnt+=len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅
            
        else :
            stack.pop()
            cnt+=1 # 두 번째 경우인 나머지 부분을 카운팅 
print(cnt)