class Solution:

    def strongPasswordCheckerII(self, password: str) -> bool:

        c1 = c2 = c3 = c4 = 0
        for c in password:
            if c.islower():
                c1 += 1
            elif c.isupper():
                c2 += 1
            elif c.isdigit():
                c3 += 1
            elif c in "!@#$%^&*()-+":
                c4 += 1

        return len(password) >= 8 and c1 > 0 and c2 > 0 and c3 > 0 and c4 > 0 and all(password[i] != password[i - 1] for i in range(1, len(password)))
