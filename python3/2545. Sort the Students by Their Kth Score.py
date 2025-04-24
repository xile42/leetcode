class Solution:

    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        kth_value_idx = [(score[idx][k], idx) for idx in range(len(score))]
        sorted_kth = sorted(kth_value_idx, key=lambda x: x[0], reverse=True)
        index_order = [i[1] for i in sorted_kth]

        return [score[idx] for idx in index_order]
