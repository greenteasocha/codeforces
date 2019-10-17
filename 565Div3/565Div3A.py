import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))


def solve():
    num = getN()
    ans = 0
    while (True):
        if num % 2 == 0:
            num = num // 2
        elif num % 3 == 0:
            num = (num // 3) * 2
        elif num % 5 == 0:
            num = (num // 5) * 4
        else:
            if num == 1:
                print(ans)
                return
            else:
                print(-1)
                return

        ans += 1


n = getN()
for i in range(n):
    solve()
