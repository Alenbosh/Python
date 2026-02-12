def rec (arr,n):
    if(n==1):
        return ("sorted array",arr)
    else:
        def rec2 (j):
            if (j==n-1):
                return rec(arr,n-1)
            else:
                if (arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                j=j+1
                return rec2(j)
        return rec2(j=0)
arr=[13,46,24,52,20,9]
n=len(arr)
t = rec(arr,n)
print(t)
