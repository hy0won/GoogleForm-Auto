board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

stack=[]
count = 0
# moves를 열로 한다
for j in moves:
    for i in range(len(board)):
        item = board[i][j-1]

        # 배열 중 값이 0이 아니면 스택에 추가한다
        if item != 0:
            stack.append(item)
            board[i][j-1] = 0
            # 반복문 탈출
            break
    # 스택의 길이가 2이상이면 맨 뒷값과 그 전 값이 같은지 아닌지 검사하고
    # 같으면 지운다    
    if len(stack)>=2:
        if stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            count+=2
# 없어진 갯수
print(count)
