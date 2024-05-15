class Solution(object):
    def similarPairs(self, words):
        
        count = 0
        char_sets = [set(word) for word in words]
        
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if char_sets[i] == char_sets[j]:
                    count += 1
                    
        return count
