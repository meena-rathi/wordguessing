import random

def random_word():
    list_words = ['programming', 'teacher', 'happy', 'world', 'hi']
    return random.choice(list_words)

def validation(word, word_length):
    try:
        if not isinstance(word, str):
            raise ValueError("Input must be a string.")
        elif " " in word:
            raise ValueError("Spaces are not allowed in the input.")
        elif len(word) != word_length:
            raise ValueError(
                f"Exactly {word_length} characters required, you provided {len(word)}"
            )
        elif not word.isalpha():
            raise ValueError("Only alphabetic characters are allowed in the input.")
        
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False
    return True

def guessing_words(word):
    guessed_word = ["-"] * len(word)
    print("Select the guessed word") 
    print(" ".join(guessed_word))
    return guessed_word

def secret_words(word):
    guessed_word = guessing_words(word)
    correct_length = len(word)
    attempt = 5 
    hint_counter = 0 
    hint_word = 3
    list_word = 4


    # word_to_guess = word
    # guessed_word = secret_words(word_to_guess)

    while attempt > 0:
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

def provide_hint(word, word_guessed):
    hint_word = random.choice(word)
    for i in range(len(word)):
        if word[i] == hint_word:
            word_guessed[i] = word[i]

    print(f"Hint: {hint_word}")
    print(' '.join(word_guessed))
for iteration in range(1, 5):
    finish_iteration = 4

    if iteration < finish_iteration:
        word_to_guess = random_word()
        guessed_word = secret_words(word_to_guess)
        print("Next string\n")

print("Finish")