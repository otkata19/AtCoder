import io
import sys

_INPUT = """\
4 5 2
3 2
3 5
"""
sys.stdin = io.StringIO(_INPUT)

listA=list(map(int,input().split()))

g_list = []
r_list = []
for _ in range(listA[2]):
    s = input().split()
    g,r = int(s[0]),int(s[1])
    g_list.append(g)
    r_list.append(r)

g_li_sorted = sorted(set(g_list))
r_li_sorted = sorted(set(r_list))
g_di = {e: i+1 for i, e in enumerate(g_li_sorted)}
r_di = {e: i+1 for i, e in enumerate(r_li_sorted)}

for i in range(listA[2]):
    print(g_di[g_list[i]],r_di[r_list[i]])
#print(g_di,r_di)
#print(len(g_list),len(r_list))

'''
while True:
    try:
        listA=list(map(int,input().split()))
        print(np.zeros((listA[0], listA[1])))
        #listA<-[1,2,2,3,1]
        #ここに逐次処理を書けばいいと思う。
    except:
        break;
        #または、quit(),os.exit()をして止める。

print(listA)
#[[1, 2, 2, 3, 1], [4, 5, 3, 4, 1, 2, 3, 4], [2, 3, 5, 6, 0, 2]]
'''