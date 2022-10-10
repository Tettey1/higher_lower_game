from game_data import data
import random
from higher_art import logo, vs


# choose random account
def get_random_account():
    """returns a random account from data"""
    return random.choice(data)


def format_data(accounts):
    """takes account and returns the values in printable format"""
    name = accounts["name"]
    description = accounts["description"]
    country = accounts["country"]
    return f"{name}, a {description}, from {country}"


# check answer
def check_answer(user_guess, a_followers, b_followers):
    """Takes guess and account followers and compares them using an if statement"""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'


score = 0
print(logo)
account_b = get_random_account()

should_continue = True
while should_continue:
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()
    print(f'Compare A: {format_data(account_a)}')
    print(vs)
    print(f'Against B: {format_data(account_b)}')

    guess = input("Who has the most followers.Type 'A' or 'B': ").lower()

    if check_answer(guess, account_a["follower_count"], account_b["follower_count"]):
        score += 1
        print(f'You Are Right. Current score: {score}')

    else:
        print(f'You are wrong. Final score: {score}')
        should_continue = False
