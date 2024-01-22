import random

def random_word():
    list_words = ['programming', 'teacher', 'happy', 'world', 'hi']
    return random.choice(list_words)
def validation(word, word_length):
    """
    The input must be a string.
    Spaces are not allowed in the input.
    The length of the input must match the specified word_length.
    Only alphabetic characters are allowed in the input.

    If any of these conditions are not met, a ValueError is raised with an appropriate
    error message. If the input passes all checks, the function returns True; otherwise,
    it returns False after printing all error messages.
    """
    error_messages = []

    if not isinstance(word, str):
        error_messages.append("Input must be a string.")

    if " " in word:
        error_messages.append("Spaces are not allowed in the input.")

    if len(word) != word_length:
        error_messages.append(
            f"Exactly {word_length} characters required, you provided {len(word)}"
        )

    if not word.isalpha():
        error_messages.append("Only alphabetic characters are allowed in the input.")

    if error_messages:
        print("Invalid input:")
        for error in error_messages:
            print(f"- {error}")
        print("Please try again.\n")
        return False

    return True
# def validation(word, word_length):
#     """
#     The input must be a string.
#     Spaces are not allowed in the input.
#     The length of the input must match the specified word_length.
#     Only alphabetic characters are allowed in the input.

#     If any of these conditions are not met, a ValueError is raised with an appropriate
#     error message. If the input passes all checks, the function returns True; otherwise,
#     it returns False after printing an error message.
#     """
#     try:
#         if not isinstance(word, str):
#             raise ValueError("Input must be a string.")
#         elif " " in word:
#             raise ValueError("Spaces are not allowed in the input.")
#         elif len(word) != word_length:
#             raise ValueError(
#                 f"Exactly {word_length} characters required, you provided {len(word)}"
#             )
#         elif not word.isalpha():
#             raise ValueError("Only alphabetic characters are allowed in the input.")
        
#     except ValueError as e:
#         print(f"Invalid input: {e}, please try again.\n")
#         return False
#     return True

def guessing_words(word):
    """Starts a word guessing game with the provided word."""
    guessed_word = ["-"] * len(word)
    print("Select the guessed word") 
    print(" ".join(guessed_word))
    return guessed_word

def provide_hint(word, word_guessed):
    """Provides a hint for the word by revealing one randomly chosen letter."""
    hint_word = random.choice(word)
    for i in range(len(word)):
        if word[i] == hint_word:
            word_guessed[i] = word[i]
    print(f"Hint: {hint_word}")
    print(' '.join(word_guessed))

def secret_words(word):
    """
    Initializes a programming-related word guessing game.
    Player has 5 attempts to guess the word, with hints after 3 incorrect attempts.
    Prompts user for input and provides feedback.
    Returns the state of guessed letters during the game.
    """
    print("This contains string words related to programming\n")
    guessed_word = guessing_words(word)
    correct_length = len(word)
    attempt = 5 
    hint_counter = 0 
    hint_word = 3
    while attempt > 0:
        print(f"{attempt} attempts remaining\n")
        user_input = input("Enter the guessed word: ")
        if user_input == word:
            print("Correct!")
            break
        else:
            print("Try again")
            attempt -= 1
        hint_counter += 1
       
        if attempt == hint_word:
            provide_hint(word, guessed_word)
            hint_counter = 0
        if not validation(user_input, correct_length):
            continue

    if attempt == 0:
        print("Sorry, you're out of attempts. The correct word was:", word)

    return guessed_word

def main():
    for iteration in range(1, 5):
        finish_iteration = 4
        if iteration < finish_iteration:
            word_to_guess = random_word()
            guessed_word = secret_words(word_to_guess)
            print("Next string\n")

    print("Finish")

if __name__ == "__main__":
    main()