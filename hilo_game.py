"""
Create a Hi-Low game, post to demostrate mastery of git.
"""

import random

def main():
    points = 300
    while points > 0:
        card = generate_first_card()
        card2 = generate_second_card()
        print(f"The card is: {card}")
        response = get_response()
        print(f"Next card was: {card2}")
        reward = allocate_points(card, card2, response, points)
        points = points + reward
        print(f"Your score is: {points}")
        keep_going = keep_playing()
        if keep_going == 2:
            break

def generate_first_card():
    card = random.randint(1,13)
    return card

def get_response():
    response = input("Higher or Lower? [h/l] ")
    return response

def generate_second_card():
    card2 = random.randint(1,13)
    return card2

def allocate_points(card, card2, response, points):
    if (card > card2 and response.lower() == 'l') or (card < card2 and response.lower() == "h"):
        reward = 100
    elif (card > card2 and response.lower() == 'h') or (card < card2 and response.lower() == "l"):
        reward = -75
    else:
        reward = 0
    return reward

def keep_playing():
    play = input("Would you like to keep playing? y/n ")
    if play.lower() == 'y':
        keep_going = 1
    else:
        keep_going = 2
    return keep_going

main()
