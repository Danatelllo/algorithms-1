def is_correct_brackets(row):
    stack = []
    open_r = ['(', '{', '[']
    open_l = [')', '}', ']']
    for j in row:
        if j in open_r:
            stack.append(j)
        elif not stack and j in open_l:
            return 'no'
        elif j in open_l and stack:
            if stack[-1] == open_r[open_l.index(j)]:
                stack.pop(len(stack) - 1)
            else:
                return 'no'

    if not stack:
        return 'yes'
    else:
        return 'no'


print(is_correct_brackets(input()))
