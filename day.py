a=[1,2,3,4,5]
n=len(a)
c=0
for i in range(n):
    for j in range(n-1):
        c=c+1
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("output  ")
for i in a:
    print(i,end=" ")
    print("total",c)