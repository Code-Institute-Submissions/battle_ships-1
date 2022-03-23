# Battleships

A simple one player python console game of Battleships. The aim is to find the battleship that has been randomly generated and hidden on seven by seven grid.

## Live Project

You can view the live project [here](https://battleships-amj.herokuapp.com/)

## How to play
On running the game the user is prompted to enter numbers between 0-6 for a row and column and has seven turns to attempt to find the hidden battleship. 

## Features
Other than the greeting message, there are a number of messages that the user can trigger (in not so polite piratey language) informing them of the following. 
- If a user makes a guess outside of the range on the board (Off the game board)
- If the user misses. 
- If the user enters a blank. 
- If the user enters something that is not a number. 

There is also a turn counter displayed after each attempt.

## Modules
I have used two modules in the making of this game
- [PyInputPlus Module.](https://automatetheboringstuff.com/2e/chapter8/) 
- [Randint](https://www.geeksforgeeks.org/python-randint-function/) which is a function of the built-in random module. 

I liked the neatness the PyInput offered. Through I understand that the same outcome could have been achieved through the normal input of allowing the user to enter a string. 
