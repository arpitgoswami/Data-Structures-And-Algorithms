class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        res = {}
        sum = 0
        count = 0
        
        for i in nums:
            sum += i
            if sum - goal in nums:
                count += res(sum-goal)
            res[i] = res.get(i, 0) + 1;
        
        return count

                
s = Solution()
print(s.numSubarraysWithSum([1,0,1,0,1], 2))
