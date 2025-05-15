class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import Counter, defaultdict

        results = defaultdict(list)
        for word in strs:
            counter = Counter(word)
            this_key = str()
            for key in sorted(counter.keys()):
                this_key += key + str(counter[key])
            results[this_key].append(word)

        return list(results.values())