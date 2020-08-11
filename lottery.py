import random

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
    for i in range(6):
        lottery_numbers.add(random.randint(0,1000000))
    return lottery_numbers
# Then we match the user number to the lottery numbers
# Calculate the winnings based on how many the user matched
print(get_players_number())

