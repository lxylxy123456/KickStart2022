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

import heapq

def count_bin(n, P):
	ans = 0
	for i in range(P):
		if n & (1 << i):
			ans += 1
	return ans

T = int(input())
for test in range(T):
	N, M, P = map(int, input().split())
	p0 = [0] * P	# complain of choosing 0
	p1 = [0] * P	# complain of choosing 1
	dp = [0] * P	# advantage of choosing 1
	for i in range(N):
		for jndex, j in enumerate(input()):
			if int(j):
				p0[jndex] += 1
				dp[jndex] += 1
			else:
				p1[jndex] += 1
				dp[jndex] -= 1
	m = set()
	for i in range(M):
		m.add(tuple(map(int, input())))
	optimal = tuple(map(lambda x: int(x > 0), dp))
	oscore = 0
	for i, j0, j1 in zip(optimal, p0, p1):
		oscore += [j0, j1][i]
	fringe = [(oscore, optimal)]
	visited = set()
	while fringe:
		sc, cand = heapq.heappop(fringe)
		# print(sc, cand)
		if cand not in m:
			ans = sc
			break
		if cand in visited:
			continue
		visited.add(cand)
		ncand = list(cand)
		for i in range(P):
			nsc = sc
			if cand[i]:
				nsc += dp[i]
			else:
				nsc -= dp[i]
			ncand[i] = 1 - ncand[i]
			heapq.heappush(fringe, (nsc, tuple(ncand)))
			ncand[i] = 1 - ncand[i]
	else:
		assert 0
	print('Case #%d:' % (test + 1), ans)

