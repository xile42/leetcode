class Solution:

    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        if event1[-1] < event2[0] or event1[0] > event2[-1]:
            return False

        return True
