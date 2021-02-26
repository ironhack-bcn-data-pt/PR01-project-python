from random import choice

class Player():
    def __init__(self, level = 4, colours = ['B', 'G', 'R', 'Y', 'W', 'P']): #mode='auto'):
        #self.mode = mode
        self.level = level
        self.colours = colours
        self.combinations = []

    
    
    def generate(self):
        code = []
        for i in range(self.level):
            code.append(choice(self.colours))
        self.code = code
        

    def guess(self):
        while True:

            ok = True
            usercode = input('\nTell me a code: ')
            
            # Do not differentiate between lower and upper cases:
            usercode = usercode.upper()

            # Check the length of the code:

            if len(usercode) > self.level:
                ok = False
                print(f'You have introduced more colours than {self.level}\n')

            elif len(usercode) < self.level:
                ok = False
                print(f'You have introduced less colours than {self.level}\n')
            else:

                # Check that the colours are inside the predefined ones
                for letter in usercode:
                    if letter not in self.colours:
                        ok = False
                        print(f'\x1b[0;37;41m {letter} does not belong to the colour code {self.colours}\n \x1b[0m')

            if ok:
                break
                
        return usercode
        
    def check(self, usercode):
    
        # Counters
        self.bulls = len([i for i,j in zip(usercode, self.code) if i == j])
        self.cows = len([i for i in usercode if i in self.code]) - self.bulls

        if self.cows < 0:
            self.cows = 0

        if self.bulls == self.level:
            return 1
        else:
            print(f'cows = {self.cows} bulls={self.bulls}')
            return 0


class Game:
    def __init__(self):
        self.name = '--------     Welcome to mastermind     --------\n'
        self.description = '''You need to guess the colour code I have thought of...\n\nHere there are some indications:
        COWS = number of correct colours but not in the good place
    	BULLS = number of correct colours and in the right place\n'''
        self.levelinstructions = '''You need to introduce your level. The options are:
        - easy : combination of 3 colours and between 4 colours
        - medium: combination of 4 colours and between 6 colours
        - advance: combination of 5 colours and between 6 colours\n'''
        self.easy = 'The colours are B, G and R\n'
        self.medium = 'The colours are B, G, R, Y, W and P\n'

    def setlevel(self):

    	while True:
	    	level = input('Introduce the level: ')

	    	if level == 'easy':
	    		self.colours = ['B', 'G', 'R']
	    		self.level = 3
	    		print(self.easy)
	    		break
	    	elif level == 'medium':
	    		self.colours = ['B', 'G', 'R', 'Y', 'W', 'P']
	    		self.level = 4
	    		print(self.medium)
	    		break
	    	elif level == 'advance':
	    		self.colours = ['B', 'G', 'R', 'Y', 'W', 'P']
	    		self.level = 5
	    		print(self.medium)
	    		break
	    	else:
	    		print('\x1b[0;37;41m' + 'The level must be easy, medium or advance \n' + '\x1b[0m')


    def play(self):

        p = Player(self.level, self.colours)
        
        # generate the code to guess
        p.generate()

        # tries counter
        self.tries = 0

        while True:
            self.tries += 1
            usercode = p.guess()
            p.check(usercode)

            # add the combination and the number of cows and bulls to show it 
            # next time if it was not right
            p.combinations.append([usercode, p.cows, p.bulls])

            # check if the input combination is the same as the original one, 
            # if so game has ended
            if ''.join(p.code) == usercode:
                print(f'Congratulations, you have guessed the code in {self.tries} tries!!')
                break

            # show the previous combinations and cows&bulls
            print('\nPrevious combinations tried:')
            print('Combinations | Cows | Bulls')
            for comb in p.combinations:
                print(f'{comb[0]}\t     | {comb[1]}    | {comb[2]}')




if __name__ == '__main__':
    game = Game()
    print(game.name)
    print(game.description)
    print(game.levelinstructions)
    # set level
    game.setlevel()

    while True:
        game.play()
        if input('Do you want to play again? (y|n)') != 'y':
            break