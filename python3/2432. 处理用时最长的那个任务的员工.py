class Solution:

    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        cur = 0
        ns = list()
        for _id, t in logs:
            ns.append([t - cur, -_id])
            cur = t
        ns.sort(reverse=True)

        return -ns[0][-1]
