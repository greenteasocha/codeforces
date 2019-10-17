import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

from bisect import bisect_left

n, m, a, b, k = getList()
anums = getList()
bnums = getList()

minpos = bnums[0] + b
maxpos = bnums[-1] + k
ans = 0

if k >= min(n,m):
    print(-1)
    sys.exit()

for i , anum in enumerate(anums):
    if i > k:
        break
    insert = bisect_left(bnums, anum + a)
    if insert + k - i >= m:
        print(-1)
        sys.exit()
    tmp = bnums[insert + k - i] + b
    if ans < tmp:
        ans = tmp
print(ans)
#
# while(maxpos - minpos > 1):
#     mid = (minpos + maxpos) // 2
#     judge(anums, bnums, k, mid)
