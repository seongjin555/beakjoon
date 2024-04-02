from collections import deque
n = int(input())
apple = int(input())
aplle_deque = deque()
for _ in range(apple):
    a, b = map(int, input().split())
    aplle_deque.append((b,a))
snake_deque = deque()
snake_deque.append((1,1))
time = 0
x_vec = 1
y_vec = 0
turn_dic = {}
turn = int(input())
for _ in range(turn):
    t, c = input().split()
    turn_dic[int(t)] = c
while True:
    if time in turn_dic:
        if turn_dic[time] == 'D':
            xy = x_vec
            x_vec = - y_vec
            y_vec = xy
        elif turn_dic[time] == 'L':
            xy = x_vec
            x_vec = y_vec
            y_vec = -xy
    x, y = snake_deque.popleft()
    snake_deque.appendleft((x, y))
    next_x, next_y = x + x_vec, y + y_vec
    time += 1
    if next_x <= 0 or next_x > n or next_y <=0 or next_y > n:
        break
    if snake_deque.count((next_x, next_y)) > 0:
        break
    try: 
        aplle_deque.remove((next_x, next_y))
        snake_deque.appendleft((next_x, next_y))
    except:
        snake_deque.appendleft((next_x, next_y))
        snake_deque.pop()
print(time)

# 정답 시도 : 1회
# 걸린시간 2시간 
        
# 사용한 자료구조 : deque
# 시간복잡도: O(N^2)
        
# https://www.acmicpc.net/problem/3190