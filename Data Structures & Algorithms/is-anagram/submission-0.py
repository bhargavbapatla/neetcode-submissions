class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        for i in s:
          if i in s_set:
            s_set[i] +=1
          else:
            s_set[i] = 1

        t_set = {}
        for j in t:
          if j in t_set:
            t_set[j] +=1
          else:
            t_set[j] = 1

        return s_set == t_set

        