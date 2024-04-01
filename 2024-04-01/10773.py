l = int(input())
L = []
for _ in range(l):
    k = int(input())
    if k == 0:
        L.pop()
    else:
        L.append(k)
print(sum(L))

# 정답 시도 : 1회
# 걸린시간 6분
        
# 사용한 자료구조 : stack
# 시간복잡도: O(N)
        
# https://www.acmicpc.net/problem/10773