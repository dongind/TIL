```python
def degree1(A,n):
    result=''
    for i in range(len(A)):
        result=result+str(A[-i-1][n])
    return result

def degree2(A,n):
    result=''
    for i in range(len(A)):
        result=result+str(A[-1-n][-1-i])
    return result

def degree3(A,n):
    result=''
    for i in range(len(A)):
        result=result+str(A[i][-1-n])
    return result

T=int(input())
for tc in range(T):
    N=int(input())
    sample=[list(map(int,input().split())) for _ in range(N)]
    print("#{}".format(tc+1))
    for i in range(N):
        print(degree1(sample,i),end=' ')
        print(degree2(sample,i),end=' ')
        print(degree3(sample,i))
```

