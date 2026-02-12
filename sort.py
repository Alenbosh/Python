arr=[7,6,5,4]
h=0
# sam=[]
k=-1
# for i in arr:
#     min=arr[0]
#     for j in arr:
#         if(j<min):
#             min=j
#     arr.remove(j)
#     sam.append(min)
# print("sorted array:",sam)
for i in range(len(arr)): #4 means [0,3]
    k+=1
    min=arr[k]
    for j in range(k,len(arr)):
        if(arr[j]<min):
            min=arr[j]
            h=j
    # h=arr.index(min)
        # print(h)
    arr[k],arr[h]=min,arr[k]
    # sam.append(min)
    # arr.remove(min)
print("sorted array:",arr)
#





