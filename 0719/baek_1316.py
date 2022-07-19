def repeat(A):
    stack = []
    sample = ''
    for i in A:
        if i not in stack :
            stack.append(i)
            sample = i
        elif i != sample :
            return 0
    return 1

N = int(input())
cnt = 0
for _ in range(N):
    test = str(input())
    if repeat(test):
        cnt += 1
print(cnt)