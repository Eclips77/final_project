import uuid

class IdFctory:
    """
    create a unique id.
    """
    @staticmethod
    def create_uuid():
        return str(uuid.uuid4())

    