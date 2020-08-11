# User can pick 6 numbers
# Lottery calculates 6 random numbers
# Then we match the user number to the lottery numbers
# Calculate the winnings based on how many the user matched

def get_players_number():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    #Create a set of int from number_csv file
    numbers = number_csv.split(",")
    integer_set = {int(number) for number in numbers}
    return integer_set

print(get_players_number())