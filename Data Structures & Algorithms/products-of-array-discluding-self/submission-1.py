class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def getProduct(pos, nums, prod):
            i = 0
            val = 1
            if pos > 0 and nums[pos] != 0:
          

                res = int(prod[pos-1] * nums[pos-1]//nums[pos])
                prod[pos]=res
                return res
            else:
                while i < len(nums):
                    if i != pos:
                        val = val * nums[i]
                    i+=1
                prod[pos]=val
                return val

        res=[]
        prod={}
        i=0
        while i < len(nums):
          res.append(getProduct(i, nums,prod))
          i+=1
        return res
        