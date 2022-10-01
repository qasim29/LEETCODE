# def productExceptSelf(self, nums: List[int]) -> List[int]:

def productExceptSelf(nums):
    parr = []
    sarr=[]
    result=[]
    prev=1
    for i in nums:
        parr.append(prev*i)
        prev=prev*i
 
    prev=1
    for i in range(len(nums)-1,-1,-1):
        sarr.insert(0,prev*nums[i])
        prev=prev*nums[i]
    print(nums)
    print(parr)
    print(sarr)

productExceptSelf([1,2,3,4])