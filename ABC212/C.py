import io
import sys

_INPUT = """\
1 1
10
10




"""
sys.stdin = io.StringIO(_INPUT)

A, B = map(int, input().split())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))
#combined3 = [abs(x-y) for x in li1 for y in li2]
#n_list = sorted(combined3)
for i in li1:
    li2.append(i)
    s_li2 = sorted(li2)
    #print(s_li2)
    small = float('inf')
    if s_li2[-1] != i:
        min_n = min(abs(i-s_li2[s_li2.index(i)-1]), abs(i-s_li2[s_li2.index(i)+1]))
        #print(min_n)
    else:
        min_n = abs(i-s_li2[s_li2.index(i)-1])
    small = min(small, min_n)
    li2.remove(i)
print(small)
#print(sorted(li1), sorted(li2))


"""
# 二つずつをひとつずらしずつ取り出す(準備) 1/2
# まず、リスト内要素をひとつずらした新規リストを2つ作成する
n = 1
x2_list = s_new_list[n:] + s_new_list[:n] # 要素のインデックスをひとつずらす
print(x2_list) # リストの先頭にあった要素が一番最後に移る
s_new_list.pop() # リストの末尾の要素を削除
x2_list.pop()

# 上記二つのリストから2つずつをひとつずらしずつ取り出す 2/2
small = float('inf')
for x1, x2 in zip(s_new_list, x2_list):
    n = abs(x1-x2)
    small = min(small, n)
    print(small)
"""