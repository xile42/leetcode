class MovingAverage:

    def __init__(self, size: int):

        self.ns = list()        
        self.size = size

    def next(self, val: int) -> float:

        self.ns.append(val)
        ns = self.ns[-self.size:]

        return 0 if len(ns) == 0 else sum(ns) / len(ns)
