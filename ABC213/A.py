import io
import sys

_INPUT = """\
10 12




"""
sys.stdin = io.StringIO(_INPUT)

li = input().split()
a,b = int(li[0]),int(li[1])
print(a ^ b)