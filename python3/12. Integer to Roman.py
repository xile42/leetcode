class Solution:

    corner_case_map = {
        4: "IV",
        9: "IX",
        40: "XL",
        90: "XC",
        400: "CD",
        900: "CM",
    }

    def handle_one_part(self, num: int) -> str:

        if num == 0:
            return ""

        if num in self.corner_case_map:
            return self.corner_case_map[num]

        if num >= 1000:
            return "".join(["M" for _ in range(num//1000)])
        elif num >= 100:
            if num < 500:
                return "".join(["C" for _ in range(num//100)])
            else:
                return "D"+"".join(["C" for _ in range((num-500)//100)])
        elif num >= 10:
            if num < 50:
                return "".join(["X" for _ in range(num // 10)])
            else:
                return "L" + "".join(["X" for _ in range((num - 50) // 10)])
        else:
            if num < 5:
                return "".join(["I" for _ in range(num // 1)])
            else:
                return "V" + "".join(["I" for _ in range((num - 5) // 1)])

    def intToRoman(self, num: int) -> str:

        result = str()
        for base_num in [1000, 100, 10, 1]:
            part_num = num // base_num * base_num
            result += self.handle_one_part(part_num)
            num -= part_num

        return result
