class Solution:

    def wordsAbbreviation(self, words: List[str]) -> List[str]:

        suoxie_dict = {}
        for word in words:
            if len(word) <= 3:
                suoxie_dict[word] = word
            else:
                for a in range(1, len(word) - 1):
                    if a == len(word) - 2:
                        suoxie = word
                    else:
                        suoxie = word[:a] + str(len(word) - a - 1) + word[-1]
                    if suoxie in suoxie_dict.keys():
                        if suoxie_dict[suoxie] != '0':
                            last_word = suoxie_dict[suoxie]
                            if a == len(word) - 3:
                                suoxie_dict[last_word] = last_word

                            else:
                                last_suoxie = last_word[:a+1] + str(len(word) - a - 2) + word[-1]
                                suoxie_dict[last_suoxie] = last_word
                            suoxie_dict[suoxie] = '0'
                        else:
                            continue
                    else:
                        suoxie_dict[suoxie] = word
                        break
        ans = {}
        for key in suoxie_dict.keys():
            if suoxie_dict[key]!='0':
                ans[suoxie_dict[key]] = key

        return [ans[word] for word in words]