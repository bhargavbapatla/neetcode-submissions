class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        set_nums = set(nums)
        nums = list(set_nums)
        s_nums = sorted(nums)
        seq = 0
        max_seq = 0
        ini = s_nums[0]
        for i in s_nums:
            if i - ini > 0 and i - ini == 1:
                seq+=1
            else:
                seq = 1

            if max_seq < seq: max_seq = seq
            ini = i
        return max_seq