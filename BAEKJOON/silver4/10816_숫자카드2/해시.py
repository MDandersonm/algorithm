#10816 숫자카드2

n=int(input())
list1= list(map(int,input().split()))
m=int(input())
list2= list(map(int,input().split()))

dic={}
for x in list1:
    if dic.get(x): #None이 아니면
        dic[x]+=1
    else:
        dic[x]=1
for y in list2:
    r= dic.get(y)
    if r: #None이 아니면
        print(r, end=' ')
    else:
        print(0, end= ' ')

