from queue import PriorityQueue
que = PriorityQueue()
n = int(input())
for _ in range(n):
    que.put(int(input()))

sum = 0
while que.qsize() > 1:
    a = que.get() + que.get()
    sum += a
    que.put(a)

print(sum)

# 정답 시도 : 1회 
# 걸린시간 40분
        
# 사용한 자료구조 : 우선순위 큐
# 시간복잡도: O(NlogN) -> 우선순위 큐의 get연산과 put연산은 logN
        
# https://www.acmicpc.net/problem/1715