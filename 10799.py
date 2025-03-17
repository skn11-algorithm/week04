# https://116116.tistory.com/entry/백준-10799번-쇠막대기-python-1
s = input()

stack = []
count = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            count += len(stack)
        else:
            count += 1
print(count)