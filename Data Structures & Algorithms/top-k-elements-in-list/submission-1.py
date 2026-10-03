class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return list({k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse = True)})[:k]
        