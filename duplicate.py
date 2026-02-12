arr = [3,4,5,5,6]
dean=arr.copy()
for i in range(len(dean)):
    dup=dean[i]
    for j in range(i+1,len(dean)):
        if(dean[j]==dup):
            arr.pop(j)
print("Non-duplicate array", arr)
