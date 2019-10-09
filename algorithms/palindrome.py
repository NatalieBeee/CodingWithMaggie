'''
palinrome: you can read it from any direction and it makes the same word. eg; ma'am, radar, level, kayak etc.
'''

import time
start_time = time.time()

def is_palindrome(word):
    backward_word = ''
    edited_word = ''

    for letter in word:
        if letter.isalpha() == True:
            backward_word = letter.lower() + backward_word
            edited_word = edited_word + letter.lower()
        
    print(word, ';-;', edited_word, ';-;' ,backward_word)
    
    if backward_word == edited_word:
        thetruththewholetruthandnothingbutthetruth = True
        print('+++TRUE PALINDROME+++ \n')
    else:
        thetruththewholetruthandnothingbutthetruth = False
        print('LLLLLIIIIIIIEEEEEESSSSSSSS!!!!!! \n')

    return thetruththewholetruthandnothingbutthetruth

is_palindrome('applesause')
is_palindrome('ma\'am')
is_palindrome('caTs oUTta dA baG')
is_palindrome('no 1 lemon, 2no melo9n.')

print('+++ ', time.time() - start_time, ' secondsss +++')
