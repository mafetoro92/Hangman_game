def hagman_code(pick_word):
    your_word = ' '
    lifes = 6  # How many life you have in the game.

    while lifes > 0:  # This loop will be working just 6 times
        mistakes = 0
        for letter in pick_word:  # Looping for every single leter the our pick_work
            if letter in your_word:
                print(letter, end=' ')
            else:
                print('*', end='')
                mistakes += 1  # Add the mistakes the player is having.

        if mistakes == 0:
            print('congratulations you win')
            break  # If we guess the word with 0 mistakes break the while loop.

        your_letter = input(' Introduce a letter')
        your_word += your_letter  # Add in the letter the player are adding.

        if your_letter not in pick_word:  # If the player take wrong word.
            lifes -= 1  # Take lives.
            print('Mistake')
            print('You have ' + str(lifes) + ' lifes')

        if lifes == 0:
            print('You lose')

    else:
        print('Thanks for your participation')
