try:
	import os, sys
	stdin = sys.stdin
	if len(sys.argv) > 1:
		stdin = open(sys.argv[1])
	else:
		# stdin = open('s.txt')
		stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

def test_win(B, N):
	# whether B wins: 0 not win; 1 win; 2 impossible
	def neighbors(p):
		x, y =p
		if x > 0:
			yield x - 1, y
		if y > 0:
			yield x, y - 1
		if x < N - 1:
			yield x + 1, y
		if y < N - 1:
			yield x, y + 1
		if x > 0 and y < N - 1:
			yield x - 1, y + 1
		if y > 0 and x < N - 1:
			yield x + 1, y - 1
	def get_item(l, p):
		return l[p[0]][p[1]]
	reachability = []	# [012 reachable from left, 012 reach from right]
	for i in range(N):
		reachability.append([])
		for j in range(N):
			reachability[-1].append([0, 0])
	def dfs(p, rindex):	# TODO
		if get_item(B, p) != 'B':
			return 0
		my_reach = get_item(reachability, p)
		if my_reach[rindex]:
			# already visited
			return my_reach[rindex]
		my_reach[rindex] = 1
		double = False
		for i in neighbors(p):
			if dfs(i, rindex) == 2:
				double = True
		if double:
			my_reach[rindex] = 2
		return my_reach[rindex]
	for i in range(N):
		dfs((i, 0), 0)
		dfs((i, N - 1), 1)
	print(*B, sep='\n')
	print(*reachability, sep='\n')
	print()
	# 0/0

T = int(input())
for test in range(T):
	N = int(input())
	B = []
	nb = 0
	nr = 0
	for i in range(N):
		B.append(list(input()))
	R = []
	for i in range(N):
		R.append([])
		for j in range(N):
			if B[j][i] == 'R':
				R[i].append('B')
				nr += 1
			elif B[j][i] == 'B':
				R[i].append('R')
				nb += 1
			else:
				R[i].append('.')
	if abs(nb - nr) >= 2:
		ans = 'Impossible'
	else:
		bw = test_win(B, N)
		rw = test_win(R, N)
		ans = nb, nr, bw, rw
	print('Case #%d:' % (test + 1), ans)

