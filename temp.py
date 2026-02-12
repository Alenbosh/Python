class Solution:
    def largestElement(self, nums):
            if (len(nums)%2==0):
                for i in range(len(nums)-1):
                    if (nums[i]>nums[i+1]):
                        nums[i],nums[i+1] =nums[i+1],nums[i]
                # print(nums[-1])
            else:
                for i in range(len(nums)-1):
                    if (nums[i]>nums[i+1]):
                        nums[i],nums[i+1] =nums[i+1],nums[i]
                # print(nums[-1])
            return nums
    n=int(input("enter the size of an array:"))
    a=[]
    for i in range(n):
        k=int(input("enter the elements:"))
        a.append(k)
    k = largestElement(1,a)
    print(k)
    
