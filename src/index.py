# Define ranks, suits, and values for a standard deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
