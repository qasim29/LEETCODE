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
    
    result.append(sarr[1])
    ptr=0
    while(ptr<len(nums)-2):
        result.append(parr[ptr]*sarr[ptr+2])
        ptr+=1
    result.append(parr[ptr])
        
    print(nums)
    print(parr)
    print(sarr)
    print(result)

productExceptSelf([1,2,3,4])