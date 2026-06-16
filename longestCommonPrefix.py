def longestCommonPrefix(strs):

    prefix = strs[0]

    for i in range(1, len(strs)):
        result = ""
        prefixlen = len(prefix)
        wordlen = len(strs[i])
        word = strs[i]
        k,j = 0,0
        while k < prefixlen and j < wordlen:
            if prefix[k] != word[j]:
                break
            else:
                result = result + prefix[k]
            k += 1
            j += 1
        prefix = result
    return prefix

strs = ["flower","flow","flight"]
# output = "fl"
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
# output = ""
print(longestCommonPrefix(strs))
