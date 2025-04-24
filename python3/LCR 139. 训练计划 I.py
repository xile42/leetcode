class Solution:

    def trainingPlan(self, actions: List[int]) -> List[int]:

        return [i for i in actions if i & 1] + [i for i in actions if not i & 1]
