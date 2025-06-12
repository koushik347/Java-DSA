def countSubarraysGreaterThanK(nums, K):
    count = 0
    n = len(nums)

    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += nums[j]
            if sum_ > K:
                count += 1
    return count
if __name__=="__main__":
    nums = [1,2,3,4]
    K=5
    print(countSubarraysGreaterThanK(nums, K))