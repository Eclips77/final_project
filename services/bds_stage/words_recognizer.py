import logging
from typing import List, Dict
logger = logging.getLogger(__name__)



class WordsDetector:
    """"
    Detect weapons in text documents and enrich them with a 'Weapons_Detected' field."""
    def __init__(self, weapons_list: List[str]):
        self.weapons_list = weapons_list

    def detect_weapons(self, documents: List[Dict],column:str="text") -> List[Dict]:
        """
        Detect weapons in the documents and enrich them with a 'Weapons_Detected' field.

        Args:
            documents (List[Dict[str, Any]]): List of documents to process.

        Returns:
            List[Dict[str, Any]]: List of enriched documents.
        """
        enriched_docs = []
        for doc in documents:
            try:
                text = doc.get(column, "")
                detected_weapons = [weapon for weapon in self.weapons_list if weapon in text]
                enriched_doc = {
                    **doc,
                    "weapons": detected_weapons
                }
                enriched_docs.append(enriched_doc)
            except Exception as e:
                logger.error(f"Error processing document {doc.get('_id')}: {e}")
                continue
        return enriched_docs
    
