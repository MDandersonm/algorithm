# from collections import *
# _,a,_,b=open(0)
# c=Counter(a.split())
# for v in b.split():
#     print(c[v])
#

from collections import*
f=lambda:map(int,input().split())
f()
c=Counter(f())
f()
print(*(c[i]for i in f()))