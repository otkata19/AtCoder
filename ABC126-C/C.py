import io
import sys

_INPUT = """\
3 10





"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())

i, n = 1, 2

f_p = 0
while i <= B:
    p = 1/A * (1/2) ** n
    i = i * 2
    n += 1
    f_p += p
    print(f_p)

print(f_p)