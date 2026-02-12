def recinser(arr,j,i,n):
    if (i==n):
        return arr 
    else:
        return rec2(arr,j,i,n)

def rec2(arr,j,i,n):
            if j==n-1:
                return recinser(arr,0,i+1,n)
            else:
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
            return rec2(arr,j+1,i,n)


arr=[13,46,24,52,20,9]
n=len(arr)
i=0
j=0
h = recinser(arr,j,i,n)
print(h)
