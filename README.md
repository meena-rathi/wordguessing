
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
    Click on the https://8000-meena-rathi-shopping-t5i0p7g8wj.us2.codeanyapp.com/index.html.
    Click on the run  button"
    Random word will appear on the screen.
    And then user has to guess the word.
    if the useer guess correct word
    Browser : chrome
    Actual result : your guess correct.
    Excepted result : your should should be correct.
    Status : Pass

2. Test Case:
    Click on the https://8000-meena-rathi-shopping-t5i0p7g8wj.us2.codeanyapp.com/index.html.
    Click on the run  button"
    Random word will appear on the screen.
    And then user has to guess the word.
    if the enter any numeric input.
    Browser : chrome
    Actual result : Numeric values are not allowed.
    Excepted result :Numeric values are not allowed .
    Status : Pass

3. Test Case:
    Click on the https://8000-meena-rathi-shopping-t5i0p7g8wj.us2.codeanyapp.com/index.html.
    Click on the run  button"
    Random word will appear on the screen.
    And then user has to guess the word.
    if the enter any input if the input is greater or smaller than the word length .
    Browser : chrome
    Actual result : Word length is not to equal to word.
    Excepted result :there should be show the message word lenth is no match to word.
    Status : Pass

4. Test Case:
    Click on the https://8000-meena-rathi-shopping-t5i0p7g8wj.us2.codeanyapp.com/index.html.
    Click on the run  button"
    Random word will appear on the screen.
    And then user has to guess the word.
    Enter string input.
    If the sring is not match to actual word.
    Browser : chrome
    Actual result : Word is not matches show message "try again" .
    Excepted result :there should be Word is not matches show message "try again" .
    Status : Pass


4. Test Case:
    Click on the https://8000-meena-rathi-shopping-t5i0p7g8wj.us2.codeanyapp.com/index.html.
    Click on the run  button"
    Random word will appear on the screen.
    And then user has to guess the word.
    Enter any input.
    after 2 apptempts of hint will be appear any random position.
    Browser : chrome
    Actual result : A random hint appear in a word.
    Excepted result :there should be a random hint appear in a word..
    Status : Pass

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
