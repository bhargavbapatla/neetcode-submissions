class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in seen:
                seen["".join(sorted(strs[i]))] = [*seen["".join(sorted(strs[i]))], strs[i]]
            else:
                seen["".join(sorted(strs[i]))] = [strs[i]]

        return [i for i in seen.values()]

        # arr = [0] * 26
        # tar = [0] * 26
        # result = []
        # added = {}
        # for i in range(len(strs)):
        #     if strs[i] in added:
        #         continue
        #     par = [strs[i]]
        #     for j in strs[i]:
        #         arr[ord(j) - ord("a")] += 1
        #     for k in range(i + 1, len(strs)):
        #         for x in strs[k]:
        #             tar[ord(x) - ord("a")] += 1
        #         if arr == tar:
        #             added[strs[k]] = 1
        #             par.append(strs[k])
        #         tar = [0] * 26
        #     arr = [0] * 26
        #     result.append(par)
        # return result
