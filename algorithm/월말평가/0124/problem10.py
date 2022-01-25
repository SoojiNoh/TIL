# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.

def get_final_position(N, mat, moves):

    def get_current_position(N, mat):
        for r in range(0,N):
            for c in range(0,N):
                if mat[r][c] == 1:
                    return c, r

    x, y = get_current_position(N, mat)

    for M in moves:
        if M==0:
            y=-1
        elif M==1:
            y+=1
        elif M==2:
            x-=1
        elif M==3:
            x+=1

    return [x,y] if 0<=x<=N-1 and 0<=y<=N-1 else None

    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]

    moves3 = [0, 0, 0]
    print(get_final_position(N, mat, moves3)) # None