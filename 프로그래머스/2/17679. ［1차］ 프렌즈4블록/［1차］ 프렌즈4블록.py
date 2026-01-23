def solution(m, n, board):
    answer = 0
    board = [list(board[i]) for i in range(m)]
    # print(board)
    
    while True:
        # 1. 지울 블록 찾기 (set 활용)
        remove = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != ' ':
                    remove.update([(i,j), (i,j+1), (i+1, j), (i+1,j+1)])
        # 2. 지울 블록이 없다면 break
        if len(remove) == 0:
            break
        
        # 3. total_removed에 지운 개수 추가
        answer += len(remove)
        
        # 4. 블록 제거 (' ' 처리)
        for r,c in remove:
            board[r][c] = ' '
        remove = set()
        
        # 5. 블록 떨어뜨리기 (빈 칸 채우기)
        for i in range(n):
            stack = []
            for j in range(m):
                if board[j][i] != ' ':
                    stack.append(board[j][i])
                    board[j][i] = ' '
            # print(stack)
            
            for k in range(m-1, -1, -1):
                if stack:
                    board[k][i] = stack.pop()
                else:
                    break
        
    return answer