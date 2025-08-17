class Solution:

    def arrangeWords(self, text: str) -> str:

        ns = [[word.lower(), i] for i, word in enumerate(text.split())]
        ns.sort(key=lambda x: [len(x[0]), x[1]])
        ns[0][0] = ns[0][0].capitalize()

        return " ".join(word for word, _ in ns)
