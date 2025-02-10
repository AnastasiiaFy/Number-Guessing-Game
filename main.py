import random


def display_welcome_message():
    print("\033[35m\tHi! Welcome to the", "\033[36mNUMBER GUESSING GAME\033[0m")
    print("\033[35m\tSo, the rules of our game are as follows:\033[0m")
    print("\033[35m\tI guess","\033[32ma number from 1 to 100\033[0m")
    print("\033[35m\tYou have to guess it in a limited number of chances.\033[0m")
    print("\033[35m\tEvery next round the range of numbers will increase!\033[0m")
    print("\033[35m\t\tGood luck!\033[0m")


def select_difficulty_level():
    print("\033[35m\nPlease select the difficulty level:")
    print("\033[32m 1. Easy level - 10 chances\033[0m")
    print("\033[33m 2. Medium level - 5 chances\033[0m")
    print("\033[31m 3. Hard level - 3 chances \033[0m")

    while True:
        level_choice = input("\033[35m\nEnter the number of the selected level (1, 2 or 3) - \033[0m").strip()

        if level_choice == "1":
            print("\033[32mGreate! You have selected easy difficulty level.\033[0m")
            return "easy", 10
        elif level_choice == "2":
            print("\033[33mGreate! You have selected medium difficulty level.\033[0m")
            return "medium", 5
        elif level_choice == "3":
            print("\033[31mGreate! You have selected hard difficulty level.\033[0m")
            return "hard", 3
        else:
            print("\033[38mYou write the wrong option. Please select 1, 2 or 3.\033[0m")


def guessing_process(numb_of_chances, upper_limit):
    number_to_guess = random.randint(1, upper_limit)
    print("\033[36m\n\tThe number is thought of.\033[0m")

    for chance in range(1, numb_of_chances + 1):
        while True:
            try:
                guess = int(input(f"\033[35m\nEnter your guess (from 1 to {upper_limit}) - \033[0m"))
            except ValueError:
                print("You write the invalid guess. Please write a number.")
            else:
                break

        if guess > number_to_guess:
            print(f"\033[37mIncorrect! Number is less than {guess}.\033[0m")
        elif guess < number_to_guess:
            print(f"\033[37mIncorrect! Number is large than {guess}.\033[0m")
        elif 1 > guess > upper_limit:
            print(f"\033[37mIncorrect! {guess} is out of range.\033[0m")
        else:
            print(f"\033[36m\nCongratulations! You guessed the correct number in {chance} attempts.\033[0m")
            return chance

    print(f"\033[35m\nSorry, you've run out of chances. The correct number was {number_to_guess}.\033[0m")
    return float('inf')


def ask_to_continue():
    while True:
        choice = input("\033[35m\nВo you want to move on to the next round? (yes/no) - \033[0m").lower().strip()

        if choice == "yes":
            return True
        elif choice == "no":
            print("\033[36mThanks for playing. I hope you enjoyed it.\n\033[0m")
            return False
        else:
            print("You write the wrong option. Please select yes or no.")


def print_high_score(high_scores):
    print("\033[0m-"*76)
    print(f"|{'\033[33mHIGH SCORE\033[0m':^83}|")
    print("-" * 76)
    print(f"|{'Level':^14}|{'Easy':^19}|{'Medium':^19}|{'Hard':^19}|")
    print("-" * 76)
    print(f"|{'Best attempt':^14}|{high_scores["easy"]:^19}|{high_scores["medium"]:^19}|{high_scores["hard"]:^19}|")
    print("-" * 76)


def main():
    display_welcome_message()

    high_scores = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf')}
    upper_limit = 100

    while True:
        difficulty_level , numb_of_chances = select_difficulty_level()

        winning_attempt = guessing_process(numb_of_chances, upper_limit)

        if winning_attempt < high_scores[difficulty_level]:
            high_scores[difficulty_level] = winning_attempt

        if not ask_to_continue():
            print_high_score(high_scores)
            break
        else:
            upper_limit += 50



if __name__ == "__main__":
    main()
