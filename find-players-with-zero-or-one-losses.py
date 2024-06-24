class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        loss_count = defaultdict(int)
        players = set()

        for winner, loser in matches:
            loss_count[loser] += 1
            players.add(winner)
            players.add(loser)

        no_loss = [player for player in players if loss_count[player] == 0]
        one_loss = [player for player in players if loss_count[player] == 1]

        return [sorted(no_loss), sorted(one_loss)]
