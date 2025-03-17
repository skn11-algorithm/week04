# 쇠막대기
# input: 괄호들
# output: 잘려진 조각의 총 개수

# 레이저는 괄호 쌍으로 표현, 쇠막대기 왼쪽 끝은 여는 괄호, 오른쪽 끝은 닫힌 괄호
# 여는 괄호 바로 다음 닫힌 괄호면 레이저이고 여는 괄호와 닫힌 괄호가 떨어져 있으면 쇠막대기

# 여는 괄호로 쇠막대기 개수를 알 수 있고, 닫힌 괄호 하나 오면 여는 괄호 개수 -1이 잘린 막대기 개수임
# 닫는 괄호 하나씩 나올 때마다 여는 괄호는 스택에서 하나씩 빼기
# 여는 괄호 3개 스택에 있고, 여는 괄호 스택에 하나 들어왔는데 닫힌 괄호가 하나 들어왔으니까 스택에 여는 괄호 하나 Pop하고 len(스택)을 쇠막대기 개수에 더하고
# 여는거 닫히는거 하나씩 들어왔으니까 또 len(스택) 더하고 닫힌거니까 하나 pop해서 뭐 이런시긍로 이어 가기


makdaeki = input()

stack = []
count = 0
for i in range(len(makdaeki)):
    if makdaeki[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if makdaeki[i-1] == '(':
            count += len(stack)
        else:
            count += 1
        
print(count)