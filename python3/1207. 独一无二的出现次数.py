class Solution:

    def uniqueOccurrences(self, arr: List[int]) -> bool:

        return len(tar := Counter(arr).values()) == len(set(tar))
