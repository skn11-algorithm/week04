import sys

def count_pieces(brackets):
    stack = []
    total_pieces = 0

    for i in range(len(brackets)):
        if brackets[i] == '(':  
            stack.append('(')
        else: 
            stack.pop() 
            if brackets[i - 1] == '(':  
                total_pieces += len(stack)  
            else:  
                total_pieces += 1  

    return total_pieces

brackets = sys.stdin.readline().strip()

print(count_pieces(brackets))
