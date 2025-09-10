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
        self.single_risky = single_risky
        self.single_very_risky = single_very_risky
        self.pair_risky = pair_risky
        self.pair_very_risky = pair_very_risky
        # self._scoring_dict = {}

    def _score_percent(self, text: str) -> float:
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
        result = (points * 100.0) / effective_words
        result = round(result, 2)
        return result
    
    def _boolean_danger_score(self,danger_percent:float)->bool:
        """
        calc if danger percents is danger

        if risk level is not none = danger.

        """
    
        return True if danger_percent >= 10 else False

    def _risk_level_score(self,danger_percent: float)->str:
        """
        calculate risk level by percents

        0 - 10 = none. one of a 10 word is risky

        10 - 20  = medium.  between 1 in 10 and 1 in 5 word is risky

        20 ++ = high. word in 5 or more is risky

        """
        if danger_percent < 10:
            return "none"
        elif danger_percent < 20:
            return "medium"
        return "high"

    def dict_builder(self,text:str):
        scoring_dict = {}
        danger_perc = self._score_percent(text)
        scoring_dict["bds_percent"] = danger_perc
        scoring_dict["is_bds"] = self._boolean_danger_score(danger_perc)
        scoring_dict["bds_threat_level"] = self._risk_level_score(danger_perc)
        return scoring_dict





if __name__ == "__main__":
    z = ["gaza"]
    s = ["gun"]
    d = [("war","crime")]
    w = [("adi","died")]

    risker = RiskScorer(z,s,d,w)
    txt = "i am in london gaza is war crime adi died  dd dd kklk lklk ggg ggg ggg gg g g g g gg gg g g"
    xxx = risker.dict_builder(txt)
    print(xxx)
