import streamlit as st
import pandas as pd
from utils import get_recommendations, load_custom_css
import os

# Page configuration
st.set_page_config(
    page_title="Makeup Recommender",
    page_icon="💄",
    layout="wide"
)

# Load custom CSS
load_custom_css()

# Navigation
page = st.sidebar.selectbox("Navigate to", ["Home", "Recommendations", "About Products"])

def get_product_image(product_name, category):
    """Get product image path or return placeholder"""
    base_path = "assets/product_images"
    placeholder_path = "assets/product_images/placeholder.svg"
    image_name = product_name.lower().replace(' ', '_') + '.jpg'
    image_path = os.path.join(base_path, category.lower(), image_name)
    return image_path if os.path.exists(image_path) else placeholder_path

def show_recommendations():
    st.title("💄 Your Perfect Makeup Match")
    st.markdown("Let's find your ideal makeup products based on your preferences!")

    # Product Type Section
    st.sidebar.header("1️⃣ Product Type")
    category = st.sidebar.selectbox(
        "What are you looking for today?",
        ["Foundation", "Lipstick", "Eyeshadow", "Mascara", "Blush", "Primer", "Bronzer", 
         "Concealer", "Setting Powder", "Highlighter", "Eyeliner", "BB Cream", "CC Cream",
         "Lip Gloss", "Contour", "Brow Products", "Setting Spray"],
        help="Choose the type of makeup you want to find"
    )

    # Skin Profile Section
    st.sidebar.header("2️⃣ Your Skin Profile")
    skin_type = st.sidebar.selectbox(
        "What's your skin type?",
        ["Normal", "Oily", "Dry", "Combination", "Sensitive", "All"],
        help="This helps us find products that work best for your skin"
    )

    # Additional Skin Concerns
    skin_concerns = st.sidebar.multiselect(
        "Any specific skin concerns?",
        ["Acne Prone", "Aging", "Dark Spots", "Large Pores", "Redness", "None"],
        default=["None"],
        help="Select multiple if applicable"
    )

    undertone = st.sidebar.radio(
        "What's your skin undertone?",
        ["Warm (golden/yellow)", "Cool (pink/red)", "Neutral (mix)", "Not Sure"],
        help="Undertone helps match you with the right shades"
    )

    # Price Range (in Rupees)
    st.sidebar.header("3️⃣ Budget")
    price_range = st.sidebar.slider(
        "What's your budget? (₹)",
        min_value=500,
        max_value=10000,
        value=(2000, 6000),
        step=500,
        help="Slide to set your minimum and maximum price range"
    )

    # Coverage and Finish options
    coverage = st.sidebar.selectbox(
        "Coverage Level",
        ["Light (natural look)", "Medium (everyday wear)", "Full (flawless finish)"]
    )
    
    finish = st.sidebar.selectbox(
        "Preferred Finish",
        ["Matte", "Dewy", "Satin", "Metallic", "Natural", "Radiant"]
    )

    if st.sidebar.button("🔍 Find My Perfect Products", type="primary"):
        with st.spinner("Finding your perfect makeup matches..."):
            # Convert price range from rupees to dollars for backend
            dollar_price_range = (price_range[0]/83, price_range[1]/83)
            recommendations = get_recommendations(
                skin_type=skin_type,
                category=category,
                price_range=dollar_price_range,
                undertone=undertone.split(" (")[0],
                coverage=coverage.split(" (")[0],
                finish=finish
            )
            if recommendations.empty:
                st.error("😕 No products found matching your criteria. Try adjusting your preferences!")
            else:
                st.success(f"🎉 Found {len(recommendations)} perfect matches for you!")

                # Display recommendations in a grid
                cols = st.columns(3)
                for idx, (_, product) in enumerate(recommendations.iterrows()):
                    with cols[idx % 3]:
                        # Get product image
                        image_path = get_product_image(product["name"], product["category"])

                        # Convert price to rupees for display
                        price_in_rupees = product["price"] * 83

                        # Generate specific product links based on category and features
                        def get_product_link(product):
                            # Return empty string since we're not using product links
                            return "#"

                        product_link = get_product_link(product)
                        match_percentage = calculate_match_percentage(product, skin_type, undertone, coverage, finish)
                        st.markdown(f"""
                        <div class='product-card'>
                            <div class='match-badge'>{match_percentage}% Match</div>
                            <img src='{image_path}' alt='{product["name"]}' class='product-image'>
                            <h3>{product["name"]}</h3>
                            <p class='brand'>{product["brand"]}</p>
                            <p class='price'>₹{price_in_rupees:.2f}</p>
                            <div class='rating'>{'⭐' * int(product["rating"])}</div>
                            <div class='details'>
                                <p><strong>Perfect Match Because:</strong></p>
                                <ul>
                                    <li>✨ Matches your {skin_type} skin type</li>
                                    <li>💫 {product["benefits"]}</li>
                                    <li>👥 {product["coverage"]} coverage as requested</li>
                                    <li>✨ {product["finish"]} finish as preferred</li>
                                </ul>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

def calculate_match_percentage(product, skin_type, undertone, coverage, finish):
    score = 0
    total_criteria = 4  # skin_type, undertone, coverage, finish
    
    if 'All' in product['skin_type'] or skin_type in product['skin_type']:
        score += 1
    if product['undertone'] == 'All' or undertone in product['undertone']:
        score += 1
    if product['coverage'] == coverage:
        score += 1
    if product['finish'] == finish:
        score += 1
        
    return int((score / total_criteria) * 100)

def show_about_products():
    st.title("About Makeup Products")
    st.markdown("""
    ### Types of Makeup Products

    1. **Foundation** - Base makeup that evens out skin tone
    2. **Concealer** - Covers blemishes and dark circles
    3. **Lipstick** - Adds color to lips
    4. **Eyeshadow** - Enhances eyes with color
    5. **Mascara** - Lengthens and volumizes lashes

    ### How to Choose Products

    - Consider your skin type
    - Know your undertone
    - Test products before buying
    - Read reviews and ingredients
    - Start with budget-friendly options
    """)

def main():
    if page == "Home":
        st.markdown("""
        <div class="home-container">
            <h1 class="main-title">✨ Welcome to Makeup Match! 💄</h1>
            <div class="welcome-content">
                <p class="tagline">Discover Your Perfect Beauty Match</p>
                <div class="features">
                    <div class="feature-item">🎯 Personalized Recommendations</div>
                    <div class="feature-item">💫 Expert Beauty Advice</div>
                    <div class="feature-item">💝 Budget-Friendly Options</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        Find your perfect makeup products with our smart recommendation system.

        ### How to Use
        1. Navigate to 'Recommendations'
        2. Enter your preferences
        3. Get personalized product matches

        ### Start Your Beauty Journey! ✨
        """)
    elif page == "Recommendations":
        show_recommendations()
    elif page == "About Products":
        show_about_products()
    elif page == "About Project":
        show_about_project()

if __name__ == "__main__":
    main()