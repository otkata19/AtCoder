import io
import sys

_INPUT = """\
7777

"""
sys.stdin = io.StringIO(_INPUT)

S = input() # ここで標準入力
num=list(S)
s = str(S)

"""
int_list = [str(i) for i in range(10)]
n_list = int_list + ["0","1","2"]
print(n_list)
"""

n_s = "0123456789012"

if(all(x==num[0] for x in num)):
    print("Weak")
elif s in n_s:
    print("Weak")
else:
    print("Strong")