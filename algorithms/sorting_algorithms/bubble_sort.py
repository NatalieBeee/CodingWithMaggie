'''blah blah blah! (look at the name)'''
'''
import datetime

a = datetime.datetime.now()
print (a)
'''

'''import functions
functions.example()'''



'''
b = datetime.datetime.now()
print (b)

c = b - a
print(c)
'''



def swap(list, i, j):
    list[i], list[j] = list[j], list[i]

def bubbleSort(cardList):
    '''
    for card in cardList:
        print(card, end = ' · ')
    '''

    for round in range(0, len(cardList) - 1):
        print('cardList', cardList)
        # going through the list from start to 2nd last

        for i in range(0, len(cardList) - 1):
            print(cardList[i], cardList[i + 1])
            if cardList[i] > cardList[i + 1]:
                swap(cardList, i, i + 1)
        round += 1

    return cardList


list_to_sort = [4, 3, 5, 2, 1]
list_to_sort = [7, 2, 5, 4, 1, 0, 3, 6, 9, 8]
list_to_sort = [3, 6, 4, 1, 6, 8, 2]
sorted_list = bubbleSort(list_to_sort)
print('SORTEEEEDDDD:', sorted_list)

