def hagman_loops(pick_word):
    your_word = ' '
    lifes = 6

    while lifes > 0:  # las vidas sean mayor a cero vamos a ejecutar el while loop
        mistakes = 0  # contador de errores que cometa la persona
        for letter in pick_word:
            if letter in your_word:  # si cada letra que encuentre en your_word  se va a;adir en la variable your_work
                print(letter, end=' ')  # end es una funcion de print lo que hace es unir palabras
            else:
                print('*', end='')  # si no encuentra en letter en your_work es una letra que ha tenido un error y se va a;adir el error
                mistakes += 1  # por el error que haga se va llenando

        if mistakes == 0:
            print('congratulations you win')
            break  # para que salga del ciclo white por que adivino la palabra

        your_letter = input(' Introduce a letter')
        your_word += your_letter  # va a;adiendo las letras a la variable your_word

        if your_letter not in pick_word:
            lifes -= 1
            print('Mistake')
            print('You have ' + str(lifes) + ' lifes')

        if lifes == 0:
            print('you lose')

    else:
        print('Thanks for your participation')
