#Find the longest common prefix string amongst an array of strings.
def longestCommonPrefix(self, strs):
    if strs == []:
        return ""

    ret = strs[0]    
    for i in range(1,len(strs)):
        l1 = len(strs[0])
        l2 = len(strs[i])
        if l1<l2:
            l = l1
        else:
            l = l2
        ret = ret[0:l]

        for j in range(l):
            if ret[j] != strs[i][j]:
                ret = ret[0:j]
                break
    return ret
