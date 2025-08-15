S = input()
can_bang = 0
for i in S:
    if i == '(':can_bang += 1
    else: can_bang -= 1
print(can_bang)