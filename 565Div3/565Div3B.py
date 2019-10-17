import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))


def solve():
    n = getN()
    nums = getList()
    cnt = [0,0]
    sanbai = 0
    for num in nums:
        if num % 3 == 1:
            cnt[0] += 1
        elif num % 3 == 2:
            cnt[1] += 1
        elif num != 0:
            sanbai += 1

    ans = min(cnt)
    ans += (max(cnt) - ans) // 3
    ans += sanbai
    print(ans)
t = getN()
for times in range(t):
    solve()