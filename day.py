# a = [10, 22, 34, 33]

# for i in range(len(a)):  # index of array
#     print(i)


# a=[10,22,34,33]
# for in range(len(a)):  #value  of array
# print (a[i])














a=[5,4,3,2,1]
n=len(a)
c=0
for i in range(n):
    f=False
    for j in range(n-1):
        c=c+1
        if a[j]>a[j+1]:
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
            f=True
    if f==False:
        break
for i in a:
    print(i,end=" ")
    print("total",c)