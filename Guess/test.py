import sys
import random

    found=False
    rand=random.randint(int(sys.argv[1]),int(sys.argv[2]))
    while(not found):
        guess = int(input('guess a number between ' + str(sys.argv[1]) + ' and ' + str(sys.argv[2] + '\n')))
        if(guess == rand):
            print('winner')
            found=True
        else:
            print('guess again')






