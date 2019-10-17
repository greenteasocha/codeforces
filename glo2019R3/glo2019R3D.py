import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))

a,b,c = getList()
print((c+min(a,b)) * 2 + (a!=b))