from collections import Counter

class Solution(object):
    def commonChars(self, words):
       
        common_count = Counter(words[0])
        
        for word in words[1:]:
            word_count = Counter(word)
            for char in common_count.keys():
                common_count[char] = min(common_count[char], word_count[char])
        
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result
