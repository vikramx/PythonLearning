l=list(map(int,input().split(" ")))
print(l)
l1=[ ]
l2=[ ]
for i in l:
    if(i%2==0):
        l1.append(i)

    else:
        l2.append(i)
print(l1)
print(l2)
