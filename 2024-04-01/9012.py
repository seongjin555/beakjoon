l = int(input())
for i in range(l):
    s = []
    vps = list(input())
    for i in vps:
        if i == "(":
            s.append(i)
        else:
            if s:
                s.pop()
            else:
                s.append(i)
                break
    if s:
        print("NO")
    else:
        print("YES")

# 정답 시도 : 1회
# 걸린시간 26분
        
# 사용한 자료구조 : stack
# 시간복잡도: O(N)
        
# https://www.acmicpc.net/problem/9012
