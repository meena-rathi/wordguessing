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
    """
    Create sheet with the player name.
    add the row correct word and Last guess word
    Check if the sheet already exit or not and convert the upper to lower case
    if not create a new sheet
    """
    username_lower = username.lower()
    worksheets = SHEET.worksheets()
    existing_worksheet = next(
        (ws for ws in worksheets if ws.title.lower() == username_lower),
        None
    )
    if existing_worksheet:
        return existing_worksheet
    else:
        worksheet = SHEET.add_worksheet(title=username, rows="100", cols="20")
        worksheet.append_row(['Correct Word', 'Last Guessed Word'])
        return worksheet


def save_data(worksheet, correct_word, last_guessword):
    """
    Save data in the worksheet
    """
    worksheet.append_row([correct_word, last_guessword])


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
    guessed_word = guessing_words(word)
    correct_length = len(word)
    attempt = 5
    hint_counter = 0
    hint_word = 3
    last_guess = ''

    while attempt > 0:
        print(f"{attempt} attempts are remaining\n")
        user_input = input("Enter the guessed word: ")
        last_guess = user_input

        if user_input == word:
            print("Correct! \n")
            break
        else:
            print("Try again, this is not a correct word \n")
            attempt -= 1
        hint_counter += 1
        if attempt == hint_word:
            provide_hint(word, guessed_word)
            hint_counter = 0
        if not validation(user_input, correct_length):
            continue

    if attempt == 0:
        print("Sorry, you're out of attempts.The correct word was:", word)
        print("\n")
    return last_guess, guessed_word


def main():

    """
    Saves the player's data, including the word to guess, the last guess,
    and the guessed word,
    in a worksheet associated with the player's username.
    After five rounds, prints "Finish" to signify the end of the game.
    """
    print("-" * 25)
    print("Welcome to the Word Guess game! \n")
    print("This is the simple word guessing game.")
    print("All words are belong from Programming words. \n")
    print("-" * 25)
    username = input("Enter the Player Name: \n")
    print("-" * 25)
    for iteration in range(1, 6):
        word_to_guess = random_word()
        last_guess, guessed_word = secret_words(word_to_guess)
        worksheet = get_user_worksheet(username)
        save_data(worksheet, word_to_guess, last_guess)
        print("Next Guessing Word \n")
    print("Finish")


if __name__ == "__main__":
    main()
