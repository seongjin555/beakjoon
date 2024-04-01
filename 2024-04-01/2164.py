import queue

N = int(input())

q = queue.Queue()

for i in range(1, N+1):
    q.put(i)

while q.qsize() > 1:
    q.get()
    q.put(q.get())
    # true false 돌려가며 할 필요없이 두줄 실행하면 되는거였음.

print(q.get())

# 정답 시도 : 3회 -> 시간조건이 빡빡해서 불필요한 연산과정을 줄여야 했음 
# 걸린시간 13분
        
# 사용한 자료구조 : queue
# 시간복잡도: O(N)
        
# https://www.acmicpc.net/problem/10773