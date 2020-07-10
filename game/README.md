<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Mastermind
*Lola López*

*bcn-data-june-2020*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project consists in the development of the Mastermind game. It includes two versions:
1. One to run via command line
2. One to run in a notebook (jupyter notebook)

## Rules
The objective is to guess the colour code within the minimum number of tries.
One player must chooses a combination (the colours can be repeated) and the other player has to guess it.
After each try, the second player gets the feedback indicating the number of:
   - Cows: For each colour which is correct but not in the good place
   - Bulls: For each colour which is correct and in the good position

## Workflow
The steps I followed to build this project were:
1. Build all the functions separately and test them
2. Once the functions were working, I tried them all together in once
3. Build the player class
4. Build the game class
5. Validation
6. Little improvements adding more comments for the users, adding level options, etc.

## Organization
To organize the work I mainly used trello (the link is below) and the first diagram flow I did it on a paper, because it helps me to write first the pseudocode on a paper and then I started writing it in a notebook.

The repository includes:
1. README file
2. source folder:
   * Mastermind.ipynb: jupyter notebook to run the game
   * mastermindgame.py: python file including the game definition to be run in the terminal

## Links

[Repository](https://github.com/LolaLop/PR01-project-python.git)   
[Trello](https://trello.com/b/uAyrNa2X/pr01-build-your-own-game)  
