from collections import deque
a, b = map(int, input().split())

# bfs -> bottom-up 방식으로 풀기
queue = deque([])
queue.append([a, 1]) # a와 연산 횟수 추가

# 1. 2를 곱한다.
# 2. 1을 수의 가장 오른쪽에 추가한다.
while queue:
    a2, cnt = queue.popleft()
    
    if a2 > b:
        continue
    elif a2 == b:
        print(cnt)
        break
    else:
        queue.append([a2 * 2, cnt + 1])
        queue.append([int(str(a2) + "1"), cnt + 1])

# 만들 수 없는 경우    
else:
    print(-1)