"""
첫번째, 1/1 (합계 2)
두번째, 1/2 -> 2/1 (합계 3)
세번째, 3/1 -> 2/2 -> 1/3 (합계 4)

함수 제작 
기능 1 
: input된 N을 두개의 숫자로 나누는 기능
기능 2
큰 숫자/1 or 1/큰 숫자 둘 중 어느 부분으로 시작할 지 판단
"""

'''def divide(N,x):
    """
    N : num that you want to divide
    x : wheter you want to start in opposite or not
        True : N-1/1 -> 1/N-1
        False : 1/N-1 -> N-1/1
    """
    result = []
    if x == False :
        for i in range(1,N):
            result.append(f'{i}/{N-i}')
    elif x == True :
        for i in range(1,N):
            result.append(f'{N-i}/{i}')
    return result'''

"""
함수를 활용하여 제작
N이 2+3+4... 보다 작아질 때 까지 분수_list를 함수를 통해 제작(계속 중첩해서 확장)
이후 분수_list 내의 N-1 요소를 반환!
"""
'''N = int(input())
check_list = []
cnt, rev = 2, True
while N > len(check_list):
    check_list += divide(cnt, rev)
    if rev == True :
        rev = False
    else :
        rev = True
    cnt += 1
print(check_list[N-1])

상기 방법은 제한시간 초과로 새로운 방안 모색 필요
'''
"""
결국 해당 숫자가 속한 곳을 확인하기 위해선 
등차수열로 증가하는 숫자를 빼면 됨!
"""
N = int(input())
num, cnt = 0, 0
while num < N :
    cnt += 1
    num += cnt
# cnt : 단계 / N-num+cnt : 번호
"""
cnt가 짝수면 1/N-1, 음수면 N-1/1
분자 + 분모 = cnt + 1
분자 = N - num + cnt / 분모 = 1 + num - Ns
"""
if cnt % 2 == 0 :
    print(f'{N - num + cnt}/{1 + num - N}')
else : 
    print(f'{1 + num - N}/{N - num + cnt}')