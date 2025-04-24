class Solution:

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        ans = [0] * numberOfUsers
        offset = 0
        offline = defaultdict(list)

        for _type, st, s in events:
            if _type == "OFFLINE":
                t = int(st)
                offline[int(s)].append([t, t + 60])

        @cache
        def is_online(i, t):
            # print("is_online", i, t, offline[i])
            for start, end in offline[i]:
                if start <= t < end:
                    return False

            return True

        for _type, st, s in events:

            if _type == "MESSAGE":
                t = int(st)
                if s == "ALL":
                    offset += 1
                elif s == "HERE":
                    for i in range(numberOfUsers):
                        if is_online(i, t):
                            ans[i] += 1
                else:
                    for i in [int(sub_s[2:]) for sub_s in s.split(" ")]:
                        ans[i] += 1

        if offset != 0:
            ans = [i + offset for i in ans]

        return ans

