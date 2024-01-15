import random

def random_word():
    list_words = ['programming', 'teacher', 'happy', 'world']
    return random.choice(list_words)
    # word = " ".join(list_words)
    # print(word)

def guessing_words(word):
    guessed_word = ["-"] * len(word)
    print("Select the guessed word") 
    print(" ".join(guessed_word))
    return guessed_word

def secret_words(guessed_word):
    word = ''.join(guessed_word)
    attempt = 5

    while(attempt > 0):
        user_input = input("Enter the guessed word: ")
  
        if user_input == word:
            print("correct")
            break
        else:
            print("Try again")
            attempt -= 1

    if attempt == 0:
        print("Sorry, you're out of attempts. The correct word was:", word)
    return guessed_word


word_to_guess = random_word()
guessed_word = guessing_words(word_to_guess)
guessed_word = secret_words(word_to_guess)