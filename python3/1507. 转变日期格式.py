import datetime


class Solution:

    def reformatDate(self, date: str) -> str:

        d, m, y = date.split(" ")
        dict_m = {v: i+1 for i, v in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
        d = int(d[:-2])
        m = dict_m[m]
        y = int(y)
        t = datetime.datetime.strptime("{}-{}-{}".format(y, m, d), "%Y-%m-%d")

        return t.strftime("%Y-%m-%d")
