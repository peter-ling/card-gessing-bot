import numpy as np
import matplotlib.pyplot as plt


curr_deck = []
cards_left = 0
single_deck = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6',
               '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J',
               'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']
num_decks = 0


def init_deck():
    global curr_deck
    global single_deck
    global num_decks
    global cards_left

    num_decks = int(input("Number of decks used by dealer: "))
    curr_deck = single_deck * num_decks
    cards_left = 52 * num_decks

    return 0

def find_next_card():
    next_card = input("Type in the card dealt (input 2-10 or JQKA), or press X to get probability of next card, and press S if dealer shuffles: ")

    return next_card

# checks if user inputted JQKA or 2-10 or X or S
def is_valid_input(input):
    global curr_deck

    if (input != '2' and input != '3' and input != '4' and input != '5' and input != '6' and input != '7' and input != '8' and input != '9' and input != '10' and input != 'J'  and input != 'Q' and input != 'K' and input != 'A' and input != 'S' and input != 'X'):
        print("Your input was not valid. Try again.")
        return False
    if (input not in curr_deck) and input != 'X' and input != 'S':
        print("There are no more instances of this card in the current deck.")
        return False
    return True

def calculate_probabilities():
    global curr_deck
    global cards_left

    count_A = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    count_J = 0
    count_Q = 0
    count_K = 0
    probs = {}

    for card in curr_deck:
        if card == '2':
            count_2 += 1
        if card == '3':
            count_3 += 1
        if card == '4':
            count_4 += 1
        if card == '5':
            count_5 += 1
        if card == '6':
            count_6 += 1
        if card == '7':
            count_7 += 1
        if card == '8':
            count_8 += 1
        if card == '9':
            count_9 += 1
        if card == '10':
            count_10 += 1
        if card == 'J':
            count_J += 1
        if card == 'Q':
            count_Q += 1
        if card == 'K':
            count_K += 1
        if card == 'A':
            count_A += 1

    probs['2'] = count_2 / cards_left
    probs['3'] = count_3 / cards_left
    probs['4'] = count_4 / cards_left
    probs['5'] = count_5 / cards_left
    probs['6'] = count_6 / cards_left
    probs['7'] = count_7 / cards_left
    probs['8'] = count_8 / cards_left
    probs['9'] = count_9 / cards_left
    probs['10'] = count_10 / cards_left
    probs['Jack'] = count_J / cards_left
    probs['Queen'] = count_Q / cards_left
    probs['King'] = count_K / cards_left
    probs['Ace'] = count_A / cards_left

    return probs




def display_probabilities():
    global curr_deck
    global cards_left
    probs = calculate_probabilities()

    plt.style.use('ggplot')
    plt.bar(probs.keys(), probs.values())
    plt.ylabel('Probability of card being dealt next')
    plt.xlabel('Card Value')
    plt.show()


    return 0

def shuffle():
    global curr_deck
    global cards_left
    global single_deck
    global num_decks

    curr_deck = single_deck * num_decks
    cards_left = 52 * cards_left

    return 0

def deal():
    global cards_left
    global curr_deck
    while cards_left > 0:
        next_card = find_next_card()

        if is_valid_input(next_card):
            if (next_card == 'X'): # Show Probabilities
                display_probabilities()
            elif (next_card == 'S'): # Shuffle Cards
                shuffle()
                print("The deck has been shuffled!")
            else:
                print(f"The last card dealt was a {next_card}")
                curr_deck.remove(next_card)
                cards_left -= 1


    return 0






def main():
    global curr_deck
    global cards_left

    init_deck()
    deal()




if __name__ == '__main__':
    main()