class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre, post=[], []
        prod=1
        for i,j in enumerate(nums):
            if i == 0:
                pre.append(1)
            else:
                pre.append(prod)
            prod = prod * j
        prod=1
        pntr = len(nums)-1
        while pntr >= 0:
            if pntr == len(nums)-1:
                post.append(1)
            else:
                post.append(prod)
            prod *= nums[pntr]
            pntr -= 1
        post = post[::-1]
        cntr = 0
        while cntr < len(nums):
            val = pre[cntr] * post[cntr]
            res.append(val)
            cntr+=1

        return res

        