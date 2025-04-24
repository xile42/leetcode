"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:

    def read(self, buf, n):

        result = list()
        while True:
            tmp = [" "] * 4
            readed = read4(tmp)
            result += tmp[:readed]
            if readed != 4 or len(result) > n:
                break

        for idx, char in enumerate(result):
            if idx >= n:
                break
            if idx < len(buf):
                buf[idx] = char
            else:
                buf.append(char)
        buf = buf[:min(len(result), n)]

        return len(buf)
