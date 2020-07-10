<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Blackjack

<img src="https://lh3.googleusercontent.com/9tm15ugwVIhwhTw8bbzqAYvO9Kcf94M0M72EeePXHpjTEMyYCNKvLwZoyPHOyqI-ccU=s180-rw"
     
*[Victor Triviño]*

*[Data Analyst Bootcamp Barcelona, June 2020]*

## Content
- [Project Description](#project-description)
- [Rules & Workflow](#rules-workflow)

## Project Description
This project is the transciption of Blackjack in Python. This project includes the fundamental functionality except for some extras such as having multiplayer or betting money against the dealer.

## Rules & Workflow
There are two participants, the player and the dealer. As a general rule, the winner is the one who gets closer to "21" without exceding this number.
1. The game starts and we show the cards of both player and dealer. Every participant is given two cards. Nonethless, the dealer shows only one card.
2. After showing the cards, player has to decide into two options:
    - if we wants to hit and so continue with having an extra card.
    - if we wants to stay.
    This question is made until the player decides to stay or has more than "21" points.
    If the player has more than "21" points, game is over and dealer wins.
3. If the player decides to stay before having "21" points, it is dealer time to play.
    Dealer has no option but to have cards until it gets to a minimum of "17" points. At that point dealer stops playing.
    When the dealer stops playing, if the dealer has more than "21" points, player wins.
    When the dealer stops playing, if the dealer has more points than player, dealer wins.
    When the dealer stops playing, if the dealer has less points than player, player wins.
     
Once the game is over, we ask the player if we wants to play again. If so, the game restarts.

Step by step is covered and commented into the game itself.


