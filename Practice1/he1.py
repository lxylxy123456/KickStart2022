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

from collections import deque

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
	# [0]: first round
		# -1: not 'B'
		# 0: default
		# 1: reachable from left in first round, record parent in [2]
		# 2: selected path by first round
	# [1]: second round
		# -1: not 'B'
		# 0: default
		# 1: reachable from left
		# 2: reachable from right
		# 3: reachable from both
	reachability = []
	for i in range(N):
		reachability.append([])
		for j in range(N):
			if B[i][j] == 'B':
				reachability[-1].append([0, 0, None])
			else:
				reachability[-1].append([-1, -1, None])
	if 'bfs':
		fringe = deque()
		for i in range(N):
			fringe.append(((i, 0), None))
		found = None
		while fringe:
			p, pp = fringe.popleft()
			my_reach = get_item(reachability, p)
			if my_reach[0] != 0:
				continue
			my_reach[0] = 1
			my_reach[2] = pp
			if p[1] == N - 1:
				found = p
				break
			for i in neighbors(p):
				fringe.append((i, p))
		if found is None:
			return 0
		i = found
		reachs = []
		while i is not None:
			my_reach = get_item(reachability, i)
			reachs.append(my_reach)
			assert my_reach[0] == 1
			my_reach[0] = 2
			i = my_reach[2]
	def dfs(p, rmask):
		# return whether get path independent
		my_reach = get_item(reachability, p)
		if my_reach[1] == -1 or (my_reach[1] & rmask):
			# already visited
			return False
		my_reach[1] |= rmask
		if my_reach[0] == 2:
			return False
		if my_reach[1] == 3:
			return True
		for i in neighbors(p):
			if dfs(i, rmask):
				return True
		return False
	for i in range(N):
		if dfs((i, 0), 1):
			return 2
		if dfs((i, N - 1), 2):
			return 2
	if 'final':
		cur = 0
		for i in reachs:
			cur |= i[1]
			i.append(cur)
		cur = 0
		for i in reversed(reachs):
			cur |= i[1]
			i.append(cur)
		count = 0
		for i in reachs:
			if 3 == i[-2] and i[-1] == 3:
				count += 1
		if count > 1:
			return 2
		return 1

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
		if bw == 2 or rw == 2:
			ans = 'Impossible'
		else:
			if bw == 1:
				if nb >= nr:
					ans = 'Blue wins'
				else:
					ans = 'Impossible'
			elif rw == 1:
				if nb <= nr:
					ans = 'Red wins'
				else:
					ans = 'Impossible'
			else:
				ans = 'Nobody wins'
	print('Case #%d:' % (test + 1), ans)

