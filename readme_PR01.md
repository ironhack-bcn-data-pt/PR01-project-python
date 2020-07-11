<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Mastermind - Revisited!
*Veronica Agnolutto*

*Data_Barcelona_june.2o*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

*Mastermind-Revisited!* consists in create a pythonic version of the *Mastermind* code-breaking game.

I choose to create a game mixing the rules of the original pencil and paper version (*Bulls&Cows*) and the modern game with pegs invented in 1970's.


#### Object of the game :dart

The object of the game is to guess a secret code consisting of a series of digits. Each guest results in feedback narrowing down the possibilities of the code. The winner is the player who solves his opponent's secret code with fewer guesses.

## Rules

Let see the rules:

#### Rules :clipboard

- **2 players** : *codemaker* vs *codebreaker* [*BC/MM*]
- **secret code**: numeric, from 3 to 5 digits [*BC*] (blanks are NOT allowed, duplicate are)
- **codemaker**: starts the game and gives feedbacks (number of digits and positions guessed) [*BC/MM*]
- **codebreaker**: tries to *guess the pattern* [*BC*] --> (digits correct in the right position [*Bulls*] / digits correct NOT in the right position [*Cows*])
- **number of games**: even (decided at the beginning of the game) [*BC/MM*]
- **switch**: when a game ends, the codemaker becomes the codebreaker [*BC/MM*]
- **turns**: twelve, ten or eight [*MM*]
- **gameflow**: once the codemaker provide a feedback, another guess is made by the codebreaker until the code is guessed [*BC/MM*]
-**winner of a game**: the first one to reveal the other's secret number in the least number of guesses [*BC*]
-**winner of Mastermind-Revisited!**: the player who wins more games [*BC/MM*]

## Workflow

#### Workflow :rocket

1. - [x] Research (Mastermind + Bulls&Cows)
2. - [x] Pseudo-code > design the game structure
3. - [x] Code game basic (loops, functions)
4. - [x] Test game (notebook+terminal)
5. - [x]  Update README > with some experiments
6. - [x]  Presentation
7. - [x]  Check all (code+README+presentation)

## Organization

#### Planning :date

Trello (constantly updated)

## Links

[Repository](https://github.com/)  
[Slides](https://drive.google.com/drive/folders/1-3pDeIjQp9MNMQCVvtrebRMLDuLVeCKz)  
[Trello](https://trello.com/b/cVNiEA6v/project-1-mastermind)  
