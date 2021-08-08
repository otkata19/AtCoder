import io
import sys

_INPUT = """\
5
3 1 4 15 9


"""
sys.stdin = io.StringIO(_INPUT)
N = int(input())
x = list(map(int, input().split()))

y = sorted(x)
s = x.index(y[-2])+1
print(N,s)