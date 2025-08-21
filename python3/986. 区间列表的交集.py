class Solution:

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = list()

        while firstList and secondList:
            if firstList[0][0] > secondList[0][0]:
                firstList, secondList = secondList, firstList

            if firstList[0][1] >= secondList[0][0]:
                ans.append([secondList[0][0], min(firstList[0][1], secondList[0][1])])
                if firstList[0][1] <= secondList[0][1]:
                    firstList.pop(0)
                else:
                    secondList.pop(0)
            else:
                firstList.pop(0)

        return ans
