class Solution:

    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        n = len(tasks) // 4
        processorTime.sort()
        a = list()
        for t in processorTime:
            a += [t] * 4
        b = sorted(tasks, reverse=True)

        return max([a[i] + b[i] for i in range(len(a))])
