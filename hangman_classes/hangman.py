import random


class Player():
    def __init__(self, wrong_letters=0, correct_letters=0):
        self.wrong_letters = wrong_letters
        self.correct_letters = correct_letters



class Game():
    def __init__(self, attempts = 6):
        self.attempts = attempts
        self.player = Player()
        self.wrong_letters_chosen = []
        self.words = ["house","bee", "elephant", "tree", "menu", "children", "story", "tennis", "kettle"]
        self.word_to_guess = random.choice(self.words)
        self.hangman = self.get_handman()

    def play(self):

        blank = [" __ " for w in range(len(self.word_to_guess))]
        print("\n" + (" ").join(blank))
        lst_to_guess = [w for w in self.word_to_guess]
        print(self.hangman[0])

        while True:

            player_guess = (input("\nTry to guess a letter!: ").lower())

            if player_guess not in lst_to_guess:

                self.player.wrong_letters = +1

                if player_guess in self.wrong_letters_chosen:
                    print("You have already mentioned that letter, please try another one")
                    player_guess = (input("\nTry to guess a letter!: ").lower())

                self.wrong_letters_chosen.append(player_guess)
                self.attempts -= 1
                if self.attempts == 0:
                    print(self.hangman[len(self.wrong_letters_chosen)])

                    print("\nSorry, you ran out of attempts!")

                    break
                else:
                    print(
                        f" Sorry! The letter '{player_guess}' is not in the secret word! You have {self.attempts} more attempts, try again!")
                    print(self.hangman[len(self.wrong_letters_chosen)])

                print(f" These are you wrong chosen letters until now: {self.wrong_letters_chosen}")


            else:
                for i in range(len(lst_to_guess)):
                    if (lst_to_guess[i]) == player_guess:
                        blank[i] = lst_to_guess[i]
                        self.player.correct_letters += 1
                        if self.player.correct_letters == len(lst_to_guess):
                            print("Congratulations!! You guessed the secret word!")

            print((" ").join(blank))



    def get_handman(self):

        return ['''


   +---+

   |   |

       |

       |

       |

       |
 =========''', '''


   +---+
   |   |

   O   |

       |   

	   |

       |
 =========''', '''


   +---+
   |   |

   O   |

   |   |

       |

       |

 =========''', '''



   +---+

   |   |

   O   |

  /|   |

       |

       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''

  +---+
   |   |

   O   |
  /|\  |
  /    |

       |
 =========''', '''


   +---+

   |   |

   O   |

  /|\  |

  / \  |

       |

  =========''']


if __name__ == '__main__':
    print("Welcome to the Hangman! Here's the secret word:")
    game = Game()
    game.play()





