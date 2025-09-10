import base64
from typing import List, Tuple

class Base64Parser:

    # @staticmethod
    def _decode(self,encoded: str) -> str:
        return base64.b64decode(encoded).decode("utf-8")

    # @staticmethod
    def _split(self,text: str) -> Tuple[List[str], List[Tuple[str, str]]]:
        singles, pairs = [], []
        for token in text.split(","):
            parts = token.strip().split()
            if len(parts) == 1:
                singles.append(parts[0])
            elif len(parts) == 2:
                pairs.append((parts[0], parts[1]))
        return singles, pairs
    
    def decode_flow(self,encoded: str)-> Tuple:
        decoded = self._decode(encoded)
        words_lists = self._split(decoded)
        return words_lists
