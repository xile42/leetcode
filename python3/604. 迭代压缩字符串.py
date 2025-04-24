class StringIterator:

    def __init__(self, compressedString: str):

        self.s = str()
        self.cur = 0

        idx = 0
        while idx < len(compressedString):
            c = compressedString[idx]
            idx += 1
            num = str()
            while idx < len(compressedString) and compressedString[idx].isdigit():
                num += compressedString[idx]
                idx += 1
            self.s += c * int(num)


    def next(self) -> str:

        if self.cur < len(self.s):
            result = self.s[self.cur]
            self.cur += 1
        else:
            result = " "

        return result
    

    def hasNext(self) -> bool:

        return self.cur < len(self.s)
