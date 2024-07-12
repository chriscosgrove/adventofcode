import requests

with open('input.txt', 'r') as file:
    entries = file.read().splitlines()

results = [];
for entry in entries:
    stack = []
    for char in entry:
        if char.isdigit():
            stack.append(char)
    if len(stack) > 0:
        if len(stack) == 1:
            results.append(int(str(stack[0])+str(stack[0])))
            stack.clear()
            continue
        results.append(int(str(stack[0]) + str(stack[len(stack)-1])))
        stack.clear()
print(sum(results))
