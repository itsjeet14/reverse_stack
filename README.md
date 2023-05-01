# reverse_stack
Concept:
🔴Reversing a Stack uses two Stacks.
Eg. Input: [1,2,3,4,5]
Output: [5,4,3,2,1]

Operation:
🔴Create a function to insert value in the stack.
🔴🔴Check if the stack is empty or not.
🔴🔴🔴If empty
🔴🔴🔴🔴🔴append value in stack.
🔴🔴🔴🔴🔴Return
🔴🔴🔴If not empty
🔴🔴🔴🔴🔴first empty the stack
🔴🔴🔴🔴🔴Call the function insert in value function again
🔴🔴🔴🔴🔴append value in stack

🟢Create a function for reverse stack.
🟢🟢Check if the stack is empty or not.
🟢🟢🟢If empty → return
🟢🟢🟢If not empty
🟢🟢🟢🟢🟢First empty the stack
🟢🟢🟢🟢🟢Call reverse stack function
🟢🟢🟢🟢🟢Call insert value in stack function
🔴Insert input and print result.
