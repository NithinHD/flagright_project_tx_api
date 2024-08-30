from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Transaction(Base):
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