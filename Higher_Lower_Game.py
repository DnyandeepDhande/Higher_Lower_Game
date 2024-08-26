from Higher_lower_art import *
from Higher_Lower_data import data
import random

print(logo)
score = 0
game_should_continue = True
item_A = random.choice(data)

while game_should_continue:
    # Ensure item_B is different from item_A
    item_B = random.choice(data)
    while item_A == item_B:
        item_B = random.choice(data)

    print(f"Compare A: {item_A['name']}, {item_A['description']}, {item_A['country']}")
    print(vs)
    print(f"Against B: {item_B['name']}, {item_B['description']}, {item_B['country']}")
    followers_guess = input("Who has more followers? Type 'A' or 'B':").lower()

    follower_count_A = item_A['follower_count']
    follower_count_B = item_B['follower_count']

    if (followers_guess == 'a' and follower_count_A > follower_count_B) or (followers_guess == 'b' and follower_count_B > follower_count_A):
        score += 1
        print(f"You're right! Current score: {score}.")
        # The correct guess becomes the next 'A'
        item_A = item_B
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")


