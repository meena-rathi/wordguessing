import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wordguess')


def get_user_worksheet(username):
    try:
        worksheet = SHEET.worksheet(username)
    except gspread.exceptions.WorksheetNotFound:
        # If the worksheet doesn't exist, create a new one
        worksheet = SHEET.add_worksheet(title=username, rows="100", cols="20")
        # Add headings to the new worksheet
        worksheet.append_row(['Correct Answer', 'Last Guessed Answer'])
    return worksheet


def save_data(worksheet, correct_answer, last_answer):
    """
    Save data to the worksheet
    """
    worksheet.append_row([correct_answer, last_answer])


def random_word():
    list_words = ['java', 'html', 'c', 'python', 'css']
    return random.choice(list_words)


def validation(word, word_length):
    """
    The input must be a string.
    Spaces are not allowed in the input.
    The length of the input must match the specified word_length.
    Only alphabetic characters are allowed in the input.

    If any of these conditions are not met, a ValueError is raised with an
    appropriate error message. If the input passes all checks,
    the function returns True;
    otherwise, it returns False after printing all error messages.
    """
    error_messages = []

    if not isinstance(word, str):
        error_messages.append("Input must be a string.")

    if " " in word:
        error_messages.append("Spaces are not allowed in the input.")

    if len(word) != word_length:
        error_messages.append(
            f"Exactly {word_length}characters required,you provided{len(word)}"
        )
    if not word.isalpha():
        error_messages.append("Only alphabetic characters are allowed")
    if error_messages:
        print("Invalid input:")
        for error in error_messages:
            print(f"- {error}")
        print("Please try again.\n")
        return False

    return True


def guessing_words(word):
    """
    Starts a word guessing game with the provided word.
    """
    guessed_word = ["-"] * len(word)
    print("Select the guessed word")
    print(" ".join(guessed_word))
    return guessed_word


def provide_hint(word, word_guessed):
    """
    Provides a hint for the word by revealing one randomly chosen letter.
    """
    hint_word = random.choice(word)
    for i in range(len(word)):
        if word[i] == hint_word:
            word_guessed[i] = word[i]
    print(f"Hint: {hint_word}")
    print(' '.join(word_guessed))


def secret_words(word):
    """
    Initializes a programming-related word guessing game.
    Player has 5 attempts to guess the word,
    and with hints after 3 incorrect attempts.
    Prompts user for input and provides feedback.
    Returns the state of guessed letters during the game.
    """
    # print("Words belong to programming languages\n")
    guessed_word = guessing_words(word)
    correct_length = len(word)
    attempt = 5
    hint_counter = 0
    hint_word = 3
    last_guess = ''

    while attempt > 0:
        print(f"{attempt} attempts remaining\n")
        user_input = input("Enter the guessed word: ")
        last_guess = user_input

        if user_input == word:
            print("Correct!")
            break
        else:
            print("Try again, this is not a correct word")
            attempt -= 1
        hint_counter += 1
        if attempt == hint_word:
            provide_hint(word, guessed_word)
            hint_counter = 0
        if not validation(user_input, correct_length):
            continue

    if attempt == 0:
        print("Sorry, you're out of attempts. The correct word was:", word)
    return last_guess, guessed_word


def main():
    print("This is the simple word guessing game.\n")
    print("All words are belong from Programming words.")
    username = input("Enter your username: \n")
    for iteration in range(1, 6):
        word_to_guess = random_word()
        last_guess, guessed_word = secret_words(word_to_guess)
        worksheet = get_user_worksheet(username)
        save_data(worksheet, word_to_guess, last_guess)
        print("Next string\n")
    print("Finish")


if __name__ == "__main__":
    main()
