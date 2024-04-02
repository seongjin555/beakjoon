a = int(input())
D = {}
for _ in range(a):
    book = input()
    if book in D:
        D[book] += 1
    else:
        D[book] = 1
max = 0
for i in D:
    if D[i] > max:
        max = D[i]
        maxbook = i
    elif D[i] == max:
        maxbook = sorted([maxbook, i])[0]
print(maxbook)

# 정답 시도 : 2회 -> 동점일 시 이름순 조건 누락 
# 걸린시간 10분 30초
        
# 사용한 자료구조 : 사전
# 시간복잡도: O(N) = 최대값만 구하는 경우에는 정렬이 더 느리다
        
# https://www.acmicpc.net/problem/1302