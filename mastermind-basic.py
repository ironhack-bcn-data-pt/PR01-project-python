#!/usr/bin/env python
# coding: utf-8

# ## Mastermind - TheMix!

# In[1]:


import random 


# In[2]:


print("\nWelcome to 'Mastermind - Revisited!")
print("Codemaker [CM] vs CodeBreaker [CB]\n ")


# #### Number of games

# In[3]:


# max number of games
max_games = 10

while True:
    try:
        game = int(input('Please, choose the number of games you want to play: '))
    except:
        print('Please, insert a valid value!')
    
    else:
        if game%2 == 0: 
            break
        else:
            print ('Please, choose an odd number of games') 


# #### Level

# In[4]:


level = int(input('Choose the difficulty of the game: EASY [1], NORMAL [2], ADVANCED [3]: \n'))

if level == 1:
    ndigit = 3
    print('Level: EASY')
elif level == 2:
    ndigit = 4
    print('Level: NORMAL')
else:
    ndigit = 5
    print('Level: ADVANCED')
    
# print(level)
print('{} digits code \n'.format(ndigit))


# #### Max number of attempts

# In[5]:


# Number of attempts (8/10/12)
while True:
    try:
        max_attempts = int(input('Maximum number of attempts in a game (8,10,12): '))
    except ValueError:
        print('Please, insert a valid value!') 
    else: 
        if max_attempts == 8:
            break
        if max_attempts == 10:
            break
        if max_attempts == 12:
            break
        else:
            print ('Please, choose a number of attempts between 8 and 12')


# #### Codemaker

# In[6]:


print('\nCODEMAKER')
code_maker = ''

for i in range(ndigit):
    choice = str(random.randint(0,9))
    code_maker +=choice
     
print(f'Codemaker code: {code_maker}')
# print(type(code_maker))


# In[7]:


import re
ndigits = len(re.findall('\d', code_maker))
# print(ndigits)


# #### Codebreaker

# In[8]:


print('\nCODEBREAKER')
# Check that the code is composed only of numbers
while True:
    try:
        code_breaker = str(input('\nPlease insert a code of {} digits: '.format(ndigits)))
        break
    except:
        pass   
print(f'Codebreaker code (first choice): {code_breaker}')      


# #### The game

# In[9]:


print('\nRULES MASTERMIND REVISITED > BULLS & COWS \n')
print('BULLS - letters correct in the right position')
print('COWS - letters correct but in the wrong position')
print('Duplicates are allowed. Blanks are NOT allowed \n')


attempt = 1
while attempt<(max_attempts):
        # counter of attempts
        code_breaker = input('Choose another code: ')
        if code_breaker != code_maker:
            num = 0
            num_pos = 0

            for x in range(4):
                # cows
                if code_breaker[x] in code_maker:
                    num +=1
                # bulls
                if code_breaker[x] in code_maker and code_breaker[x] == code_maker[x]:
                    num_pos +=1

            print('Number guessed [C]: {} \nNumbers + positions guessed [B]: {}'.format(num,num_pos))     
            attempt +=1

        else:
            print('Congratulations! You guess the code in {} attempts'.format(attempt)) 
            break
else:
    print('Sorry! You have reached the maximum number of attempts. The codemaker wins!')


# In[ ]:




