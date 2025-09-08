import uuid
import hashlib

class IdFctory:
    """
    create a unique id.
    """
    @staticmethod
    def create_uuid():
        return str(uuid.uuid4())

    @staticmethod
    def create_hash(name:str):
        return str(hash(name))