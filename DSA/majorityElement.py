class Solution(object):
    def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] =1
        tall = len(nums)//3
        a=[]
        for i in nums:
            if(freq[i]>tall):
                if i in a:
                    continue
                else:
                    a.append(i)
        print(a)

    n=[3,2,3]
    majorityElement(n)
