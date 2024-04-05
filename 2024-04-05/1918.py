str = input()
stack = []
for i in str:
	if i == '(':
		stack.append(i)
	elif i == ')':
		while True:
			k = stack.pop()
			if k == '(':
				break
			else:
				print(k, end='')
	elif i == '*' or i =='/':
		if len(stack) != 0 and (stack[-1] == '*' or stack[-1] == '/'):
			print(stack.pop(), end = '')
		stack.append(i)
	elif i == '+' or i == '-':
		if len(stack) == 0:
			stack.append(i)
		else: 
			if stack[-1] == '+' or stack[-1] == '-':
				print(stack.pop(), end = '')
			elif stack[-1] == '*' or stack[-1] == '/':
				for _ in range(len(stack)):
					k = stack.pop()
					if k == '(':
						stack.append('(')
						break
					else:
						print(k, end='')
			stack.append(i)
	else:
		print(i, end='')
for _ in range(len(stack)):
	print(stack.pop(), end = '')
	

# 정답 시도 : 2회 -> 동등한 우선순위일 경우에 앞이 우선이어야 하는 조건 누락
# 걸린시간 40분 
        
# 사용한 자료구조 : stack
# 시간복잡도: O(N)
        
# https://www.acmicpc.net/problem/1918
