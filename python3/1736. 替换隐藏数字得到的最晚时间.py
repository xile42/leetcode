class Solution:

    def maximumTime(self, time: str) -> str:

        result = str()

        c = time[0]
        result += ("2" if time[1] == "?" or time[1] <= "3" else "1") if c == "?" else c

        c = time[1]
        result += ("9" if result[-1] != "2" else "3") if c == "?" else c

        result += ":"

        c = time[3]
        result += "5" if c == "?" else c

        c = time[4]
        result += "9" if c == "?" else c

        return result
