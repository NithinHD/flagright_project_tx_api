from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Transaction(Base):
    """
    Represents a transaction.

    Attributes:
        transaction_id (int): The unique identifier for the transaction.
        amount (float): The amount of the transaction.
        description (str): The description of the transaction.
        date_time (datetime): The date and time of the transaction.
        user_id (int): The user ID associated with the transaction.
        country (str): The country associated with the transaction.
        tags (str, optional): The tags associated with the transaction.
    """
    __tablename__ = 'transactions'
    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    date_time = Column(DateTime, default=datetime.now(datetime.UTC))
    user_id = Column(Integer, nullable=False)
    country = Column(String, nullable=False)
    tags = Column(String, nullable=True)

# Database setup
DATABASE_URL = "sqlite:///transactions.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)