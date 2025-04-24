class Solution:

    def compress(self, chars: List[str]) -> int:

        idx = 0
        results = str()
        while idx < len(chars):
            cur = chars[idx]
            idx += 1
            cnt = 1
            while idx < len(chars) and chars[idx] == cur:
                idx += 1
                cnt += 1
            results += cur
            if cnt > 1:
                results += str(cnt)

        for _ in range(len(chars)):
            chars.pop(0)

        for char in results:
            chars.append(char)
            
        return len(results)
            
        
