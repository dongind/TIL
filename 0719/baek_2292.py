N = int(input())
cnt = 0
while N > 0 :
    N = N - 6 * (cnt) -1
    cnt += 1
print(cnt)