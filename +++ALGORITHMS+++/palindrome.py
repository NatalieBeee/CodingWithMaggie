'''
palinrome: you can read it from any direction and it makes the same word. eg; ma'am, radar, level, kayak etc.
'''

def is_palindrome(word):
    backward_word = ''
    for letter in word:
        backward_word = letter + backward_word

    
    if backward_word == word:
        thetruththewholetruthandnothingbutthetruth = True
        print('+++TRUE PALINDROME+++')
    else:
        thetruththewholetruthandnothingbutthetruth = False
        print('LLLLLIIIIIIIEEEEEESSSSSSSS!!!!!!')

    return thetruththewholetruthandnothingbutthetruth

is_palindrome('applesause')
is_palindrome('ma\'am')


'''
TO DO:
deal with spaces in a palindrome.
eg, 'ele hoohele'
'''