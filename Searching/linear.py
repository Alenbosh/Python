arr=[4,5,6,7,7,8]
se=int(input("Enter a choice of no."))
flag=1
for i in range(len(arr)):
    if(arr[i]==se):
        print(se,"is present at index",i,end = " ")
        flag=0
if(flag==1):
    print(-1)
