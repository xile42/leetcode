class Solution:

    def splitIntoFibonacci(self, num: str) -> List[int]:

        n = len(num)
        mx = 2 ** 31 - 1  # 最大值为2^31-1

        def dfs(i, path):
            if i == n:
                # 只有当路径至少有3个数字时才有效
                return len(path) >= 3

            # 如果当前路径已经有至少2个数字，计算下一个期望值
            if len(path) >= 2:
                expected = path[-2] + path[-1]
                # 如果期望值超过最大值，直接返回失败
                if expected > mx:
                    return False

                # 尝试匹配期望值
                if i + len(str(expected)) > n:
                    return False

                actual_str = num[i:i + len(str(expected))]
                # 检查是否有前导零（除非期望值本身就是0）
                if actual_str[0] == '0' and expected != 0:
                    return False

                actual = int(actual_str)
                if actual == expected:
                    path.append(actual)
                    if dfs(i + len(actual_str), path):
                        return True
                    path.pop()
                return False

            # 对于前两个数字，尝试所有可能的拆分
            for j in range(i, n):
                # 检查是否有前导零（除非数字本身就是0）
                if num[i] == '0' and j > i:
                    break

                cur_str = num[i:j + 1]
                cur = int(cur_str)
                if cur > mx:
                    break

                path.append(cur)
                if dfs(j + 1, path):
                    return True
                path.pop()

            return False

        path = []
        if dfs(0, path) and len(path) >= 3:
            return path

        return []