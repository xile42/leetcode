class Solution:

    def isWinner(self, player1: List[int], player2: List[int]) -> int:

        scores1 = list()
        scores2 = list()
        for idx, (s1, s2) in enumerate(zip(player1, player2)):
            if idx >= 2:
                s1 = 2 * s1 if player1[idx - 1] == 10 or player1[idx - 2] == 10 else s1
                s2 = 2 * s2 if player2[idx - 1] == 10 or player2[idx - 2] == 10 else s2
            elif idx >= 1:
                s1 = 2 * s1 if player1[idx - 1] == 10 else s1
                s2 = 2 * s2 if player2[idx - 1] == 10 else s2
            scores1.append(s1)
            scores2.append(s2)
        print(scores1, scores2)
        if sum(scores1) > sum(scores2):
            return 1
        elif sum(scores1) < sum(scores2):
            return 2
        else:
            return 0
