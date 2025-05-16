class Solution:

    def sockCollocation(self, sockets: List[int]) -> List[int]:

        ret = reduce(xor, sockets)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in sockets:
            if n & div:
                a ^= n
            else:
                b ^= n

        return [a, b]
