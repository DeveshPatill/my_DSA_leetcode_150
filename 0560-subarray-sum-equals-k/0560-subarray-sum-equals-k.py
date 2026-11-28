class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        dic = {}
        curr_sum = 0
        for i in nums:
            if curr_sum + i == k:
                ans += 1
            if ((curr_sum + i) - k) in dic:
                ans += dic[((curr_sum + i) - k)]
            
            curr_sum += i
            dic[curr_sum] = dic.get(curr_sum,0) + 1
        return ans

        


            
