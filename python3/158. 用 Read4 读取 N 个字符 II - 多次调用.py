# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:


class Solution:
    all_buf = str()
    cur = 0

    def read(self, buf: List[str], n: int) -> int:

        buff = [""] * 4
        while (cnt := read4(buff)) > 0:
            for i in range(cnt):
                self.all_buf += buff[i]

        ans = self.all_buf[self.cur:self.cur + n]
        for i in range(len(ans)):
            buf[i] = ans[i]
        self.cur += n

        return len(ans)
