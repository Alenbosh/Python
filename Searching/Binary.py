def Binarysearch(arr,low,high,target):
    if low > high:
        return -1 
    
    mid=low+(high-low)//2
    if(arr[mid]==target):
        return mid
    elif arr[mid]<target:
        return Binarysearch(arr,mid+1,high,target)
    elif arr[mid]>target:
        return Binarysearch(arr,low,mid-1,target)
    else:
        return -1

rr=[2,3,4,5,6,7]
g=len(rr)
m=int(input("Enter the no:"))
u=Binarysearch(rr,0,g-1,m)
print("Target At index:",u)
