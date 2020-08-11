import random

def menu():
    #Ask player for numbers
    #Calculate lottery numbers
    #Print out the winnings
    player_numbers = get_players_number()
    lottery_numbers = create_lottery_numbers()
    lottery_numbers
    matched_numbers = lottery_numbers.intersection(player_numbers)
    if len(matched_numbers) == 0:
        print("No numbers matched")
    match = [int(number) for number in matched_numbers]
    prize = len(match) ** 10
    print(f"Numbers matched are: {match}, You won {prize} bananas!")


# User can pick 6 numbers
def get_players_number():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    #Create a set of int from number_csv file
    numbers = number_csv.split(",")
    integer_set = {int(number) for number in numbers}
    return integer_set


# Lottery calculates 6 random numbers
def create_lottery_numbers():
    lottery_numbers =set()
    while len(lottery_numbers) < 6:
        lottery_numbers.add(random.randint(0,10))
    return lottery_numbers

# Then we match the user number to the lottery numbers
# Calculate the winnings based on how many the user matched
menu()