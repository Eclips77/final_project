from pymongo import MongoClient
from pymongo.database import Database
from .. import config
import logging

logger = logging.getLogger(__name__)

class DatabaseConnection:
    """
    MongoDB connection manager
    """
    
    def __init__(self):
        """
        Initialize database connection
        """
        self.client = None
        self.database = None
        logger.info("init start..")
    
    def connect(self) -> Database:
        """
        Establish connection to MongoDB
        
        Returns:
            Database: MongoDB database instance
        """
        try:
            self.client = MongoClient(config.MONGO_URI)
            self.database = self.client[config.MONGO_DB]
            # Test the connection
            self.client.admin.command('ping')
            logger.info(f"connection success to db {self.database}")
            return self.database
        except Exception as e:
            raise ConnectionError(f"Failed to connect to MongoDB: {e}")
    
    def disconnect(self):
        """
        Close database connection
        """
        if self.client:
            self.client.close()