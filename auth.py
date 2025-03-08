from werkzeug.security import generate_password_hash, check_password_hash
from models import User, UserPreference
import streamlit as st
from sqlalchemy.orm import Session
import os

def init_auth():
    if 'user' not in st.session_state:
        st.session_state.user = None

def create_user(session: Session, username: str, email: str, password: str) -> User:
    """Create a new user"""
    hashed_password = generate_password_hash(password)
    user = User(
        username=username,
        email=email,
        password_hash=hashed_password
    )
    session.add(user)
    session.commit()
    return user

def authenticate_user(session: Session, username: str, password: str) -> bool:
    """Authenticate a user"""
    user = session.query(User).filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        st.session_state.user = user
        return True
    return False

def save_user_preferences(
    session: Session,
    user_id: int,
    skin_type: str,
    undertone: str,
    coverage: str,
    finish: list,
    price_range: tuple,
    concerns: list
):
    """Save or update user preferences"""
    pref = session.query(UserPreference).filter_by(user_id=user_id).first()
    
    if not pref:
        pref = UserPreference(user_id=user_id)
        session.add(pref)
    
    pref.skin_type = skin_type
    pref.undertone = undertone
    pref.preferred_coverage = coverage
    pref.preferred_finish = finish
    pref.price_range_min = price_range[0]
    pref.price_range_max = price_range[1]
    pref.concerns = concerns
    
    session.commit()

def load_user_preferences(session: Session, user_id: int) -> UserPreference:
    """Load user preferences"""
    return session.query(UserPreference).filter_by(user_id=user_id).first()
