
'''
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

total = num1 * num2

if total > 1000:
    total = num1 + num2
print('The result is', total)
#six lines
'''

'''
def find_total(num1, num2):
    total = num1 * num2

    if total > 1000:
        total = num1 + num2

    return total


print(find_total(5, 777))
print(find_total(10, 20))
#seven lines
'''


'''
num_list = [110, 40, 52, 1, 1000]
# num_list = [0, 1, 2, 3, 4, 5]
def sum_current_previous(num_list):

    print(num_list[0])
    for i in range(1, len(num_list)):
        print(num_list[i] + num_list[i-1])


sum_current_previous(num_list)


#Expected:
#110
#150
#92
#53
#1001
'''


firstList = [5, 8, 3, 9, 5, 13, 23]
secondList = [6, 2, 9, 12, 15, 21]

def findUnique (firstList, secondList):
    """ docstring
    Prints whether values in firstList are unique or not.

    TODO (o0O.O0o):
    - It only checks whether values are repeated across lists, it doesn't check whether the value appears in the same list.
    - Doesn't check uniqueness of values in secondList

    :param firstList: list of ints
    :param secondList: list of ints
    :return:
    """

    #simon said JUMP!!! #criss cross applesause

    for i in range(0, len(firstList)):
        isUnique = True

        for o in range(0, len(secondList)):
            if firstList[i] == secondList[o]:
                isUnique = False
                break
            else:
                pass
        print(isUnique)


findUnique(firstList, secondList)


print(findUnique.__doc__)
help(findUnique)
