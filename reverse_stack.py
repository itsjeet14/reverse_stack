def insert_value(stack, value):
    if not stack:
        stack.append(value)
        return
    temp = stack.pop()
    insert_value(stack, value)
    stack.append(temp)

def reverse_stack(stack):
    if not stack:
        return
    
    temp = stack.pop()
    reverse_stack(stack)
    insert_value(stack, temp)

stack = list(map(int, input("Enter element separated by space: ").split()))
print("Origingal Stack: ", stack)
reverse_stack(stack)
print("Reversed Stack: ",stack)