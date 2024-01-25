
## Purpose of the project ##

This project aims to create a word guessing game with 5 random words, offering players 5 attempts to guess each word. After 2 incorrect guesses, a hint will be revealed at a random point. The correct word and the last guessed word will be saved in a Google Sheet for tracking.

## User Story ##

I as a user, to see the infromation about game in the main page.

## Features ##

**Home**
1. Using Google sheet, Sheet will be created with the name of Player name.
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

I used Heroku to deploy the project.

## Testing ##

**Code Validation**

1. No errors in run.py file.

**Test cases**

1. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name:
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. if the user guess correct word
    6. The gusse word and actual word save in Sheet.
    7. Browser : chrome
    8. Actual result : your word guess correct.
    9. Excepted result : your word Guess should be correct.
    10. Status : Pass

2. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. If the enter any numeric input.
    6. The gusse word and actual word save in Sheet.
    7. Browser : chrome
    8. Actual result : Numeric values are not allowed.
    9. Excepted result :Numeric values are not allowed .
    10. Status : Pass

3. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. If the enter any input if the input is greater or smaller than the word length.
    6. The gusse word and actual word save in Sheet.
    7. Browser : chrome
    8. Actual result : Word length is not to equal to word.
    9. Excepted result :there should be show the message word lenth is no match to word.
    10. Status : Pass

4. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. Enter string input.
    6. If the sring is not match to actual word.
    7. The gusse word and actual word save in Sheet.
    8. Browser : chrome
    9. Actual result : Word is not matches show message "try again" .
    10. Excepted result :there should be Word is not matches show message "try again" .
    11. Status : Pass


5. Test Case:
    1. Click on the https://guess-word-922a70a849de.herokuapp.com/.
    2. Enter the Player name.
    3. Random word will appear on the screen.
    4. And then user has to guess the word.
    5. Enter any input.
    6. After 2 apptempts of hint will be appear any random position.
    7. The gusse word and actual word save in Sheet.
    8. Browser : chrome
    9. Actual result : A random hint appear in a word.
    10. Excepted result :there should be a random hint appear in a word..
    11. Status : Pass

## Fixed Bugs ##
1. Fixed the validation.
2. Fixed the provide_hint function.
3. Fixed the main function.
4. Fixed the loop to display all list item one by one.
5. Fixed issues to save data in google sheet.

## Supported Screen and browser ##

1. The website is compatible with all devices.

![Responsive](readme-doc/responsive.JPG)

## Deployment ##

**Github**
1. Locate the GitHub repository you need.
2. Click the down arrow on the "Code" button.
3. Copy the link provided in the dropdown.
4. Open your preferred code editor (like Codeanywhere) and select the directory for the clone.
5. In the terminal, use the command 'git clone' and paste the copied GitHub link.
6. Press 'Enter' to create a local clone of the repository in your chosen directory.

**Deployment**
1. Open the Heroku Account.
2. Create the heroku Account.
3. Create a app in the Heroku.
4. Go to the setting tab if use the CREDS.json paste the json code in config Var.
5. Add the bulidpack (puthon, nodeJS)
6. Go to the deploy tab select the gitHub.
7. Open the gitHub account and connect the git repositery. 
8. Deploy branch.

## Credits ##
1. Love sandwitches
2. w3 school