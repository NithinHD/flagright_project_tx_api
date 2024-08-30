from apscheduler.schedulers.background import BackgroundScheduler
from models import SessionLocal, Transaction
import random

def generate_transaction():
    """
    Generates a new transaction with random amount, description, user ID, country, and tags.
    
    Returns:
        None
    """
    session = SessionLocal()
    new_transaction = Transaction(
        amount=random.uniform(1.0, 1000.0),
        description="Auto-generated transaction",
        user_id=random.randint(1, 100),
        country="US",
        tags="auto"
    )
    session.add(new_transaction)
    session.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(generate_transaction, 'interval', seconds=1)
scheduler.start()