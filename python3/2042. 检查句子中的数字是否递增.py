class Solution:

    def areNumbersAscending(self, s: str) -> bool:

        ns = [int(w) for w in s.split(" ") if w.isdigit()]

        return all(ns[i] > ns[i - 1] for i in range(1, len(ns)))
