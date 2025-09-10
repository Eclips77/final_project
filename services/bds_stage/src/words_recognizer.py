from typing import List, Tuple

class RiskScorer:
    """
    risk scorer class for risk percent calculate
    """

    def __init__(
        self,
        single_risky: List[str],
        single_very_risky: List[str],
        pair_risky: List[Tuple[str, str]],
        pair_very_risky: List[Tuple[str, str]],
    ):
        self.single_risky = set(w.lower() for w in single_risky)
        self.single_very_risky = set(w.lower() for w in single_very_risky)
        self.pair_risky = set((a.lower(), b.lower()) for a, b in pair_risky)
        self.pair_very_risky = set((a.lower(), b.lower()) for a, b in pair_very_risky)

    def score(self, text: str) -> float:
        """
        Calculate risk percentage for given text.

        Args:
            text (str) the given text to calculate danger percent
        Returns:
                score (float) the danger score
        """
        tokens = text.lower().split()
        n = len(tokens)
        i = 0
        points = 0
        pairs_found = 0

        while i < n:
            if i + 1 < n:
                pair = (tokens[i], tokens[i + 1])
                if pair in self.pair_very_risky:
                    points += 2
                    pairs_found += 1
                    i += 2
                    continue
                elif pair in self.pair_risky:
                    points += 1
                    pairs_found += 1
                    i += 2
                    continue

            if tokens[i] in self.single_very_risky:
                points += 2
            elif tokens[i] in self.single_risky:
                points += 1
            i += 1

        effective_words = n - pairs_found
        if effective_words == 0:
            return 0.0
        return (points * 100.0) / effective_words
    


# if __name__ == "__main__":
#     z = ["gaza"]
#     s = ["gun"]
#     d = [("war","crime")]
#     w = [("adi","died")]

#     risker = RiskScorer(z,s,d,w)
#     txt = "i am in london gaza is war crime dd dd kklk lklk"
#     abd =risker.score(txt)
#     print(f" txt {abd:.2f} percent danger")