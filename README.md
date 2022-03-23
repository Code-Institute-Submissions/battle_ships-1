# Battleships

A simple one player python console game of Battleships for my third project in The Code Institue Diploma in Software Development (E-commerce Applications). 

The aim is to find the battleship that has been randomly generated and hidden on seven by seven grid.

## Deployment
The game has been depolyed to Heroku
You can view the live project [here](https://battleships-amj.herokuapp.com/)

![Heroku](assets/HEROKU.png)

## How to play
On running the game the user is prompted to enter numbers between 0-6 for a row and column and has seven turns to attempt to find the hidden battleship. 

## Features
Other than the greeting message, and the option to replay the game when finished, there are a number of messages (in not so polite pirate speak) that the user can trigger informing the user of the following. 

- If a user makes a guess outside of the range on the board (Off the game board)

![OffMap](assets/off_the_map.png)


- If the user misses. 

![Miss](assets/miss.png)


- If the user hits. 
- If the user enters a blank.

![Blank](assets/blank.png) 


- If the user enters something that is not a number. 

![String](assets/word.png)


- If the user enters the same guess at any point. 

![Same_Guess](assets/same.png)


- Game over if the user has used all seven guesses. 

![Game_Over](assets/game_over.png)


- If the user doesn't type Y/N when asked to replay

![Replay](assets/replay.png)


There is also a turn counter displayed after each attempt.

![Turn_count](assets/turn.png)


## Testing
The add has been extensively play tested and the code shows no errors when run through [PEP8 online check](http://pep8online.com/checkresult)

![PEP8](assets/PEP8.png)


## Modules
I have used one module in the making of this game

- [Randint](https://www.geeksforgeeks.org/python-randint-function/) which is a function of the built-in random module for genertating random intergers. 

## Things I have learnt in the making of this game. 
- I had initially used [PyInputPlus Module.](https://automatetheboringstuff.com/2e/chapter8/) after exploring how to show input error messages, but with some gentle nudging from a tutor decided to use input methods instead as they are much simpler. It did however give me the chance to learn about importing modules, installing them to the requirments.txt and how to fix an error by pulling and freezing. 
- Unsused variables errors 'x' can be fixed by using _ as Pylint will ignore it [Stackoverflow](https://stackoverflow.com/questions/56542190/unused-variable-i-pylintunused-variable)
- Using the "\n" newling character to for added readability [Flexple](https://flexiple.com/python-new-line/#:~:text=In%20Python%2C%20the%20new%20line,displayed%20in%20a%20new%20line.)
- The correct implementation of docstrings [Vald-phoenix](https://vald-phoenix.github.io/pylint-errors/plerr/errors/basic/C0114.html)
- The Python String join method to remove commas and quotations from lists [Geeksforgeeks](https://www.geeksforgeeks.org/python-string-join-method/)
- How to wrap long lines in Pythong [Tutorialspoint](https://www.tutorialspoint.com/How-to-wrap-long-lines-in-Python#:~:text=The%20preferred%20way%20of%20wrapping,using%20a%20backslash%20looks%20better.)

## Credits
The base code was written while doing a tutorial from [Codeacademy's](https://www.codecademy.com/courses/learn-python/lessons/battleship/exercises/welcome-to-battleship) tutorial on "How to make a battleship game in Python". 

## Errors and future changes
- There is one error that shows. 'ms-toolsai.jupyter extension is not synced, but not added in gitpod.yml' I think this is to do with Google Sheets and the templated provided. But it does not effect the app in anyway so I have decided to ingnore it. 
- I would like to create a boarder so the text isn't so squashed to the left. 
- I like to add multiplayer functions also. 
- a grid would also make the game easier on the eye. 