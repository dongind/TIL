```python
def test_row(A):
    test_list=[0]*10
    for i in A:
        test_list[i]=1
    if sum(test_list)==9:
        return 1
    return 0

def test_box(A,x,y):
    result=0
    for i in range(x,x+3):
        for j in range(y,y+3):
            result+=A[i][j]
    if result==45:
        return 1
    return 0


T=int(input())
for tc in range(1,T+1):
    sudoku=[list(map(int,input().split())) for _ in range(9)]
    result=1
    #가로 검사
    for i in sudoku:
        if not test_row(i):
            result=0
    #세로 검사
    for i in range(9):
        new_sudoku=[]
        for j in range(9):
            new_sudoku.append(sudoku[j][i])
        if not test_row(new_sudoku):
            result=0
    #영역 검사
    for i in range(3):
        for j in range(3):
            x,y=i*3,j*3
            if not test_box(sudoku,x,y):
                result=0
    print("#{} {}".format(tc,result))
```

