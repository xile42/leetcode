class Solution:

    def findStrobogrammatic(self, n: int) -> List[str]:

        d = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}
        
        def f(n):
            
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            base = ["0", "1", "8"] if n & 1 else [""]
            sub_results = f(n-2)
            results = list()
            for k, v in d.items():
                for sub_result in sub_results:
                    results.append(k + sub_result + v)

            return results

        results = f(n)
        results = [i for i in results if len(i) == 1 or (len(i) > 1 and i[0] != "0")]

        return results

##        if n == 1:
##            return ["0","1","8"]
##        
##        s1 = ["1", "6", "8", "9"]
##        s2 = ["1", "6", "8", "9", "0"]
##        s3 = ["1", "8", "0"]
##        d = {"1": "1", "6": "9", "8": "8", "9": "6", "0": "0"}
##        n2 = n // 2
##        
##        def f(n2, cur):
##
##            if n2 == 0:
##                pres.append("".join(cur))
##                return
##
##            tar = s1 if len(cur) == 0 else s2
##            for char in tar:
##                f(n2 - 1, cur + [char])
##
##        pres = list()
##        f(n2, list())
##        posts = list()
##        for pre in pres:
##            post = str()
##            for c in pre[::-1]:
##                post += d[c]
##            posts.append(post)
##
##        results = list()
##        for pre, post in zip(pres, posts):
##            if n & 1:
##                for c in s3:
##                    results.append(pre + c + post)
##            else:
##                results.append(pre + post)
##
##        return results
            
