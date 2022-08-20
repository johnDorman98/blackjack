# Imports needed for the program.
import random

# This function is used to deal cards one at a time.
def deal_card():
    """Uses the list of cards to randomly select one to be returned.

    Returns:
        int: The random number that has been chosen from the list of cards.
    """
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    return random.choice(cards)

# This function taks in a hand of cards and is used to calculate the score of that hand.
def calculate_score(hand):
    """Takes in a a hand in the form of a list and returns the sum for the total of the hand.

    Args:
        hand (list): This represents the cards that are within the hand. E.g. [2, 2]

    Returns:
        int: This uses the sum() function to return the total sum of the hand which is used for calculating the score.
    """
    
    score = sum(hand)
    
    if score == 21 and len(hand) == 2:
        return 0
    
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        
    return sum(hand)

# This function determins the winner of the game.
def compare_hands(user_score, dealer_score):
    """Compares the user and dealer score to determin the winner and returns the outcome.

    Args:
        user_score (int): This is the users hand in the form of their score.
        dealer_score (int): This is the dealers hand in the form of their score.

    Returns:
        str: Depending on the outcome returns a different message.
    """
        
    if user_score == dealer_score:
        return "Its a draw!"
    elif dealer_score == 0:
        return "Sorry you lose, Dealer wins with Blackjack."
    elif user_score == 0:
        return "You win! You won with Blackjack!"
    elif user_score > 21:
        return "Sorry you lose, you went over 21."
    elif dealer_score > 21:
        return "You win, dealer went over 21."
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose."

# This is the main function for the game and when calls starts the game.
def play_blackjack():
    """This is the main function that calls the other methods and handles all of the inputs from the user.
    """
    
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Variables which will store the cards.
    user_cards = []
    dealers_cards = []
    
    # This is used to keep track of the current state of the game.
    is_game_over = False

    # Inital two cards are delt to the user and dealer each.
    for starting_hand in range(2):
        user_cards.append(deal_card())
        dealers_cards.append(deal_card())

    while not is_game_over:
        # Store the score based on the cards in the users and dealers hands.
        users_score = calculate_score(user_cards)
        dealers_score = calculate_score(dealers_cards)

        # Display starting cards and score.
        print(f"Your cards: {user_cards}, Current score: {users_score}")
        print(f"Dealer's first card: {dealers_cards[0]}")

        # If condition to check if game is over.
        if dealers_score == 0 or users_score == 0 or users_score > 21:
            is_game_over = True
        
        # This else allows the user to take another card.
        else:
            draw_again = input("Would you like to draw another card. Type 'y' for yes, or type 'n' for no.").lower()
            
            if draw_again == "y":
                # If another card is taken the card is then added to the users hand.
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # After the user is done while the dealer does not have Blackjack and less 17 the dealer draws cards.
    while dealers_score < 17 and dealers_score != 0:
        dealers_cards.append(deal_card())
        dealers_score = calculate_score(dealers_cards)
    
    # Prints the final hands and cards, along with the final outcome of the game.
    print(f"Your final hand {user_cards}. Final score: {users_score}")
    print(f"Dealers final hand {dealers_cards}. Final score: {dealers_score}")
    print(compare_hands(users_score, dealers_score))

# Asks the user if they want to play Blackjack to start a new game.
while input("Would you like to play Blackjack. Type 'y' for yes, or type 'n' for no.").lower() == "y":
    """If the user types 'y' to play another game it calls the 'play_blackjack()' method to start again.
    """
    play_blackjack()