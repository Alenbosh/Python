def main(nums):
    candidate=None
    count=0
    for num in nums:
        if count ==0:
             candidate = num
        count +=(1 if candidate==num else -1)
    return candidate

nums=[1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,5,56,6,5,5,5,5,5,5,5,67,7,77,7,7,7,7,7]
sav = main(nums)
print(len(nums))
print(sav)