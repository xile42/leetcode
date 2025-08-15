class Solution:

    def specialPalindrome(self, n: int) -> int:

        if n == 0:
            return 1

        sn = str(n)
        base_length = len(sn)

        def generate_palindrome(s, length):

            if not length & 1:
                sn = s + s[::-1]
            else:
                part1 = s[:-1]
                center = s[-1]
                part2 = part1[::-1]
                sn = part1 + [center] + part2
            s = "".join(str(x) for x in sn)

            return int(s)

        for length in range(base_length, 46):
            ans = None
            for r in range(1, 10):
                for comb in combinations(range(1, 10), r):

                    total = sum(comb)
                    if total != length:
                        continue

                    if not length & 1:
                        valid = True
                        for d in comb:
                            if d & 1:
                                valid = False
                                break
                        if not valid:
                            continue
                        c = None
                    else:
                        odd_count = 0
                        odd_d = None
                        for d in comb:
                            if d & 1:
                                odd_count += 1
                                odd_d = d
                        if odd_count != 1:
                            continue
                        c = odd_d

                    x = dict()
                    if not length & 1:
                        for d in comb:
                            x[d] = d // 2
                    else:
                        for d in comb:
                            if d == c:
                                x[d] = (d + 1) // 2
                            else:
                                x[d] = d // 2

                    if not length & 1:
                        multiset = list()
                        for d in comb:
                            multiset += [d] * x[d]
                    else:
                        multiset = list()
                        for d in comb:
                            count = x[d]
                            if d == c:
                                count -= 1
                            if count > 0:
                                multiset += [d] * count

                    if length > base_length:
                        if not length & 1:
                            num = generate_palindrome(sorted(multiset), length)
                            if ans is None or num < ans:
                                ans = num
                        else:
                            s = sorted(multiset) + [c]
                            num = generate_palindrome(s, length)
                            if ans is None or num < ans:
                                ans = num
                    else:
                        perms = set(permutations(multiset))
                        perms = sorted(perms)
                        found = False
                        cur_ans = inf
                        for perm in perms:
                            if not length & 1:
                                num = generate_palindrome(list(perm), length)
                            else:
                                s = list(perm) + [c]
                                num = generate_palindrome(s, length)
                            if num > n:
                                if not found:
                                    cur_ans = num
                                    found = True
                                else:
                                    if num < cur_ans:
                                        cur_ans = num
                                break
                        if found:
                            if ans is None or cur_ans < ans:
                                ans = cur_ans

            if ans is not None:
                return ans
