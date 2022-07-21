"""
1           1개 => 이 부분이 특수
2 7         6개
8 19        12개
20 37       18개
38

예를 들어,
N = 13
1. 13 - 1 = 12
2. 12 - 6 = 6
3. 6 - 12 = 0

"""



N = int(input())
cnt = 0
while N > 0:
    if cnt == 0 :
        N = N - 1
        cnt += 1
    else :
        N = N - cnt * 6
        cnt += 1
print(cnt)