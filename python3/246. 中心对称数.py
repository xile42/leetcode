class Solution:
    
    def isStrobogrammatic(self, num: str) -> bool:

        lr = {0, 1, 6, 8, 9}

        sn = set(list(map(int, num)))
        if len(sn-lr) != 0:
            return False
        
        lr_num = str()
        for char in num:
            if char == "6":
                lr_num += "9"
            elif char == "9":
                lr_num += "6"
            else:
                lr_num += char
        return lr_num[::-1] == num
        
