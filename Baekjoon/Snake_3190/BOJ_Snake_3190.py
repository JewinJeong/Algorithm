def turn_direct(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

n = int(input())
k = int(input())

data = [[0] * (n + 1) for _ in range(n+1)]
# map info
for i in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1  # apple

l = int(input())
list_turn = []
for i in range(l):
    a, b = map(str, input().split())
    list_turn.append((int(a), b))
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 1, 1 # 초기 위치
data[x][y] = 2 # 뱀이 있는 위치는 2
direction = 0 # 초기 방향 동
time = 0
index = 0
q = [(x,y)] # 뱀이 있는 위치

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2: # 범위 내에 있고 내가 있는 위치기 아니면
        # 사과 있으면 이동 후 꼬리 그대로
        if data[nx][ny] == 1:
           data[nx][ny] = 2
           q.append((nx, ny))
        # 사과 없으면 이동 후  꼬리 짜르기
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            q.append((nx, ny))
            qx, qy = q.pop(0)
            data[qx][qy] = 0
    else:
        time += 1
        break
    x, y = nx, ny
    time += 1
    if index < l and time == list_turn[index][0]:
        direction = turn_direct(direction, list_turn[index][1])
        index += 1

print(time)
