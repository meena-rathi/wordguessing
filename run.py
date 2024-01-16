import random

def random_word():
    list_words = ['programming', 'teacher', 'happy', 'world']
    return random.choice(list_words)
    # word = " ".join(list_words)
    # print(word)
def validation(word, word_length):
    try:
        if len(word) != word_length:
             raise ValueError(
                f"Exactly {word_length } values required, you provided {len(word)}"
            )

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return true
def guessing_words(word):
    guessed_word = ["-"] * len(word)
    print("Select the guessed word") 
    print(" ".join(guessed_word))
    return guessed_word

def secret_words(word):
    guessed_word = guessing_words(word)
    correct_length = len(word)
    #word = ''.join(guessed_word)
    attempt = 5
    hint_word = 2

    while(attempt > 0):
        user_input = input("Enter the guessed word: ")
        if not validation(user_input, correct_length):
            break
  
        if user_input == word:
            print("correct")
            break
        else:
            print("Try again")
            attempt -= 1
        
        if attempt == hint_word:
            provide_hint(word, guessed_word)
    if attempt == 0:
        print("Sorry, you're out of attempts. The correct word was:", word)
    return guessed_word

def provide_hint(word, word_guessed):
    hint_word = random.choice(word)
    for i in range(len(word)):
        if word[i] == hint_word:
            word_guessed[i] = word[i]

    print(f"hint{hint_word}")
    print(''.join(word_guessed))

word_to_guess = random_word()
#guessed_word = guessing_words(word_to_guess)
guessed_word = secret_words(word_to_guess)