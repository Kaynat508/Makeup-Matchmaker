import pandas as pd
import numpy as np

def initialize_product_database():
    """
    Create a comprehensive makeup product database with direct product links
    """
    products = {
        'name': [
            'Maybelline Fit Me Matte Foundation', 'Maybelline SuperStay Matte Ink',
            'Swiss Beauty Ultimate Eyeshadow Palette', 'Maybelline Colossal Mascara',
            'SUGAR Contour De Force Blush', 'L\'Oreal Infallible Foundation',
            'Lakme 9 to 5 Primer + Matte Lipstick', 'Swiss Beauty Eyeshadow Palette',
            'Lakme Eyeconic Curling Mascara', 'MyGlamm Superfoods Blush',
            'Lakme Absolute Blur Primer', 'SUGAR Matte Attack Lipstick',
            'MARS Glitter Eyeshadow', 'L\'Oreal Paris Telescopic Mascara',
            'SUGAR Contour De Force Bronzer'
        ],
        'brand': [
            'Maybelline', 'Maybelline', 'Swiss Beauty', 'Maybelline', 'SUGAR',
            'L\'Oreal', 'Lakme', 'Swiss Beauty', 'Lakme', 'MyGlamm',
            'Lakme', 'SUGAR', 'MARS', 'L\'Oreal', 'SUGAR'
        ],
        'category': [
            'Foundation', 'Lipstick', 'Eyeshadow', 'Mascara', 'Blush',
            'Foundation', 'Lipstick', 'Eyeshadow', 'Mascara', 'Blush',
            'Primer', 'Lipstick', 'Eyeshadow', 'Mascara', 'Bronzer'
        ],
        'price': [
            45.99, 22.99, 38.99, 19.99, 28.99, 52.99, 24.99, 42.99, 21.99, 32.99,
            35.99, 26.99, 44.99, 23.99, 34.99
        ],
        'rating': [
            4.5, 4.2, 4.8, 4.0, 4.3, 4.6, 4.1, 4.7, 4.4, 4.2, 4.3, 4.5, 4.6, 4.2, 4.4
        ],
        'skin_type': [
            'All', 'All', 'All', 'All', 'All', 'Dry,Sensitive', 'All', 'All',
            'Oily,Combination', 'Dry,Normal', 'All', 'Sensitive', 'All', 'Sensitive', 'All'
        ],
        'coverage': [
            'Full', 'Full', 'Medium', 'Full', 'Light', 'Medium', 'Medium', 'Full',
            'Full', 'Light', 'Light', 'Full', 'Medium', 'Full', 'Medium'
        ],
        'finish': [
            'Matte', 'Matte', 'Metallic', 'Satin', 'Dewy', 'Dewy', 'Satin', 'Metallic',
            'Matte', 'Dewy', 'Radiant', 'Velvet', 'Glitter', 'Natural', 'Satin'
        ],
        'undertone': [
            'Neutral', 'Warm', 'All', 'All', 'Cool', 'Warm', 'Neutral', 'All',
            'All', 'Warm', 'All', 'Cool', 'All', 'All', 'Warm'
        ],
        'key_ingredients': [
            'Hyaluronic Acid, SPF 30', 'Vitamin E, Jojoba Oil', 'Mica, Pearl Powder',
            'Keratin, Biotin', 'Rose Extract, Vitamin C', 'Ceramides, Peptides',
            'Shea Butter, Collagen', 'Coconut Oil, Vitamin E', 'Bamboo Extract, Peptides',
            'Aloe Vera, Vitamin B5', 'Niacinamide, Collagen', 'Argan Oil, Vitamin E',
            'Pearl Powder, Mica', 'Castor Oil, Peptides', 'Cocoa Butter, Vitamin D'
        ],
        'benefits': [
            '24hr Wear, Oil Control', 'Transfer-proof, Moisturizing', 'High Pigment, Blendable',
            'Volumizing, Lengthening', 'Natural Glow, Long-lasting', 'Anti-aging, Hydrating',
            'Moisturizing, Plumping', 'Intense Color, Buildable', 'Waterproof, Smudge-proof',
            'Buildable, Natural Finish', 'Pore Blurring, Hydrating', 'Long-wear, Non-drying',
            'Multi-dimensional Shine', 'Natural Extension Look', 'Sun-kissed Glow, Buildable'
        ]
    }

    return pd.DataFrame(products)