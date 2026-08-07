import random
from art import logo, vs
from game_data import data

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
continue_game = True
acc_b = random.choice(data)

while continue_game:

    acc_a = acc_b
    acc_b = random.choice(data)

    if acc_a == acc_b:
        acc_b = random.choice(data)

    a_followers = acc_a['follower_count']
    b_followers = acc_b['follower_count']

    print(f"Compare A: {format_data(acc_a)}")
    print(vs)
    print(f"Against B: {format_data(acc_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)

    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final score: {score}")
