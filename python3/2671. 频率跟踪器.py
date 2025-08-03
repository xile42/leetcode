class FrequencyTracker:

    def __init__(self):

        self.cnt = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:

        self.cnt[number] += 1
        self.freq[self.cnt[number]] += 1
        self.freq[self.cnt[number] - 1] -= 1
        if self.freq[self.cnt[number] - 1] == 0:
            del self.freq[self.cnt[number] - 1]

    def deleteOne(self, number: int) -> None:

        if number in self.cnt:
            self.cnt[number] -= 1
            if self.cnt[number] == 0:
                del self.cnt[number]
            self.freq[self.cnt[number]] += 1
            self.freq[self.cnt[number] + 1] -= 1
            if self.freq[self.cnt[number] + 1] == 0:
                del self.freq[self.cnt[number] + 1]

    def hasFrequency(self, frequency: int) -> bool:

        return frequency in self.freq

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)