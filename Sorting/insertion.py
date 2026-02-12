arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(0,n):
    for j in range(0,n-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted array:",arr)
