def digit_stack(commands):
    stack = []
    summa = 0

    for command in commands:
        command = command.split(' ')

        if command[0] == 'PUSH':
            stack.append(int(command[1]))
        elif command[0] == 'POP' and stack:
            summa += stack.pop()
        elif command[0] == 'PEEK' and stack:
            summa += stack[-1]

    return summa

#   tests
print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK", "PUSH 9",
                   "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))
print(digit_stack(["POP", "POP"]))
print(digit_stack(["PUSH 9", "PUSH 9", "POP"]))
print(digit_stack([]))