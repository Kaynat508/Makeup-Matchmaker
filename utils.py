import streamlit as st
import pandas as pd
from data import initialize_product_database

def load_custom_css():
    """Load custom CSS styles"""
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_data
def get_recommendations(skin_type, category, price_range, undertone, coverage=None, finish=None, concerns=None):
    """
    Enhanced product recommendation system with more flexible matching
    """
    df = initialize_product_database()
    filtered_df = df.copy()

    # Map user-friendly coverage options to database values
    coverage_map = {
        "Light (natural look)": "Light",
        "Medium (everyday wear)": "Medium",
        "Full (flawless finish)": "Full",
        "Light": "Light",
        "Medium": "Medium",
        "Full": "Full"
    }

    # Map user-friendly undertone options to database values
    undertone_map = {
        "Warm (golden/yellow)": "Warm",
        "Cool (pink/red)": "Cool",
        "Neutral (mix)": "Neutral",
        "Not Sure": "All"
    }

    # Basic category filter (keep this as strict match)
    filtered_df = filtered_df[filtered_df['category'] == category]

    # Price range filter with flexible matching
    price_min, price_max = price_range
    
    # If no products in exact range, expand range by 20%
    if filtered_df[(filtered_df['price'] >= price_min) & (filtered_df['price'] <= price_max)].empty:
        price_buffer = (price_max - price_min) * 0.2
        price_min = max(0, price_min - price_buffer)
        price_max = price_max + price_buffer
    
    filtered_df = filtered_df[
        (filtered_df['price'] >= price_min) & 
        (filtered_df['price'] <= price_max)
    ]

    # Handle skin type with more flexibility
    if skin_type != "All":
        skin_type_mask = (
            filtered_df['skin_type'].str.contains(skin_type, case=False, na=False) |
            filtered_df['skin_type'].str.contains('All', case=False, na=False)
        )
        if not filtered_df[skin_type_mask].empty:
            filtered_df = filtered_df[skin_type_mask]

    # Handle coverage with more flexibility
    clean_coverage = coverage_map.get(coverage, coverage)
    coverage_mask = filtered_df['coverage'] == clean_coverage
    if not filtered_df[coverage_mask].empty:
        filtered_df = filtered_df[coverage_mask]

    # Handle undertone with more flexibility
    clean_undertone = undertone_map.get(undertone, undertone)
    if clean_undertone != "All":
        undertone_mask = (
            filtered_df['undertone'].str.contains(clean_undertone, case=False, na=False) |
            filtered_df['undertone'].str.contains('All', case=False, na=False)
        )
        if not filtered_df[undertone_mask].empty:
            filtered_df = filtered_df[undertone_mask]

    # Handle finish preferences with more flexibility
    if finish:
        finish_mask = filtered_df['finish'].str.contains(finish, case=False, na=False)
        if not filtered_df[finish_mask].empty:
            filtered_df = filtered_df[finish_mask]

    # Handle special concerns with more flexibility
    if concerns:
        concerns_mask = filtered_df['benefits'].str.contains('|'.join(concerns), case=False, na=False)
        if not filtered_df[concerns_mask].empty:
            filtered_df = filtered_df[concerns_mask]

    # If still no products found, return top rated products in the category within price range
    if filtered_df.empty:
        filtered_df = df[
            (df['category'] == category) &
            (df['price'] >= price_range[0]) &
            (df['price'] <= price_range[1])
        ]

    # Sort by rating and then price
    filtered_df = filtered_df.sort_values(
        ['rating', 'price'],
        ascending=[False, True]
    )

    return filtered_df.head(6)