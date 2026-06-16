from ast import List
from collections import defaultdict


def groupAnagram(strs: List[str]) -> List[str]:

    anagram = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        anagram[tuple(count)].append(word)
    return list(anagram.values())

strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagram(strs))

strs = [""]
# output = [[""]]
print(groupAnagram(strs))

strs = ["a"]
# output = [["a"]]
print(groupAnagram(strs))