"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:

    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def f(node):

            return node.importance + sum([f(d[subordinate]) for subordinate in node.subordinates])

        d = dict()
        for node in employees:
            d[node.id] = node

        return f(d[id])
