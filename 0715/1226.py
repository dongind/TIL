for tc in range(1,11):
    N=int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    # 출발 지점 찾기
    for i in range(16):
        for j in range(16):
            if maze[j][i]==2:
                start_x,start_y=i,j

    # 이동 방향 설정
    move=[(1,0),(0,1),(-1,0),(0,-1)]
    stack=[]
    stack.append([start_x,start_y])
    result=0

    while stack:
        x,y=stack.pop()
        maze[y][x]=1
        for dx,dy in move:
            new_x,new_y=x+dx,y+dy
            if maze[new_y][new_x]==3:
                result=1
                break
            if maze[new_y][new_x]==0:
                stack.append([new_x,new_y])
                continue
            else:
                continue
        else:
            continue
        break

    print("{} {}".format(N,result))