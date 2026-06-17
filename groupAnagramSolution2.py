# groupAnagram Solution 2 without using any inbuilt methods

def get_char_counts(word):
    char_counts = {}
    for word in word.lower():
        char_counts[word] = char_counts.get(word, 0) + 1
    return char_counts

def counts_are_equal(c1, c2):
    if len(c1) != len(c2):
        return False
    for key in c1:
        if key not in c2 or c1[key] != c2[key]:
            return False
    return True

def group_anagram(words):

    groups = []
    signature = []
    for word in words:
        count = get_char_counts(word)
        placed = False
        for i in range(len(groups)):
            if counts_are_equal(signature[i], count):
                groups[i].append(word)
                placed = True
                break
        if not placed:
            groups.append([word])
            signature.append(count)
    return groups




words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagram(words)
for group in result:
    print(group)