import abc
from abc import ABC, abstractmethod

"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):

    def __init__(self, s):

        self.s = s

    # define your fields here
    def evaluate(self) -> int:

        st = list()
        for c in self.s:
            if c.isdigit():
                st.append(c)
            else:
                b = st.pop(-1)
                a = st.pop(-1)
                st.append(str(eval(a + c + b)))

        return int(float(st[-1]))

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""


class TreeBuilder(object):

    def buildTree(self, postfix: List[str]) -> 'Node':

        return Node(postfix)


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
