from sqlalchemy import create_engine, Column, Integer, String, Float, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import os
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    created_at = Column(String, default=lambda: datetime.utcnow().isoformat())
    
    # Relationship with preferences
    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")

class UserPreference(Base):
    __tablename__ = 'user_preferences'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    skin_type = Column(String(50))
    undertone = Column(String(50))
    preferred_coverage = Column(String(50))
    preferred_finish = Column(JSON)  # Store as JSON array
    price_range_min = Column(Float)
    price_range_max = Column(Float)
    concerns = Column(JSON)  # Store as JSON array
    
    # Relationship with user
    user = relationship("User", back_populates="preferences")

# Database setup
def init_db():
    database_url = os.getenv('DATABASE_URL')
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    
    # Create session factory
    Session = sessionmaker(bind=engine)
    return Session()

# Create database tables
if __name__ == '__main__':
    init_db()
