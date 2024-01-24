
## Purpose of the project ##

This project aims to create a word guessing game with 5 random words, offering players 5 attempts to guess each word. After 2 incorrect guesses, a hint will be revealed at a random point. The correct word and the last guessed word will be saved in a Google Sheet for tracking.

## User Story ##

I as a user, 

## Features ##

**Home**
1. Sheet will be created with the name of Player name.
2. A list contains of words.
3. Each a word has a 5 attempts.
4. After 2 attemps hint will be reveal.
5. Validation handle in all cases.
6. Acutual word and player last guessed word for all words will be saved in google sheet.
7. For every player new sheet will be created.

## Technologies ##

1. I have used python language.
2. Google Sheet API.

**Github**

I used to store the code.

**CodeAnyWhere**

I used codeanywhere to develop the website.

**Heroku**

## Testing ##

**Code Validation**

1. No errors in py file.

**Test cases**

1. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name:
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. if the useer guess correct word
    6. Browser : chrome
    7. Actual result : your guess correct.
    8. Excepted result : your should should be correct.
    9. Status : Pass

2. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. If the enter any numeric input.
    6. Browser : chrome
    7. Actual result : Numeric values are not allowed.
    8. Excepted result :Numeric values are not allowed .
    9. Status : Pass

3. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. If the enter any input if the input is greater or smaller than the word length.
    6. Browser : chrome
    7. Actual result : Word length is not to equal to word.
    8. Excepted result :there should be show the message word lenth is no match to word.
    9. Status : Pass

4. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. Enter string input.
    6. If the sring is not match to actual word.
    7. Browser : chrome
    8. Actual result : Word is not matches show message "try again" .
    9. Excepted result :there should be Word is not matches show message "try again" .
    10. Status : Pass


5. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. Enter any input.
    6. After 2 apptempts of hint will be appear any random position.
    7. Browser : chrome
    8. Actual result : A random hint appear in a word.
    9. Excepted result :there should be a random hint appear in a word..
    10. Status : Pass

## Fixed Bugs ##
1. Fixed the validation.
2. Fixed the provide_hint function.
3. Fixed the main function.
4. Fixed the loop to display all list item one by one.

## Supported Screen and browser ##

1. The website is compatible with all devices.

## Deployment ##

**Github**
1. Locate the GitHub repository you need.
2. Click the down arrow on the "Code" button.
3. Copy the link provided in the dropdown.
4. Open your preferred code editor (like Codeanywhere) and select the directory for the clone.
5. In the terminal, use the command 'git clone' and paste the copied GitHub link.
6. Press 'Enter' to create a local clone of the repository in your chosen directory.

## Credits ##
1. Love sandwitches
