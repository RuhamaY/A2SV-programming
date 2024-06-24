class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n = len(piles) // 3
        max_coins = 0
        
        for i in range(n, 3 * n, 2):
            max_coins += piles[i]
        
        return max_coins
