class Solution:

    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:

        if sx == tx and sy == ty:
            return 0

        ans = list()
        q = deque()
        q.append((tx, ty, 0))
        while q:
            tx, ty, ops = q.popleft()
            if not (tx >= sx and ty >= sy):
                continue

            if tx == sx and ty == sy:
                ans.append(ops)
                continue

            if tx == ty:
                q.append((0, ty, ops + 1))
                q.append((tx, 0, ops + 1))

            elif tx > ty:
                if tx >= 2 * ty:
                    if tx % 2 == 0:
                        tx //= 2
                        q.append((tx, ty, ops + 1))
                    else:
                        return -1
                else:
                    tx -= ty
                    q.append((tx, ty, ops + 1))

            else:
                if ty >= 2 * tx:
                    if ty % 2 == 0:
                        ty //= 2
                        q.append((tx, ty, ops + 1))
                    else:
                        return -1
                else:
                    ty -= tx
                    q.append((tx, ty, ops + 1))

        return min(ans) if ans else -1
