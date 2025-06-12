def maxproduct(nums):
    if not nums:
        return 0
    maxprod=nums[0]
    minprod=nums[0]
    res=nums[0]

    for i in range(1,len(nums)):
        num=nums[i]
        if num < 0:
            maxprod,minprod=minprod,maxprod
        maxprod=max(num,maxprod*num)
        minprod=min(num,minprod*num)
        res=max(res,maxprod)
    return res
if __name__=="__main__":
    nums = [1,2,3,4]
    print(maxproduct(nums))