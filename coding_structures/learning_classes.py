
# 'python classes.py'


# defining the customer class
class Customer:
    def __init__(self, name, balance):
        self.balance = balance
        self.name = name


    def deposit(self, amount):
        # balance = balance + amount
        self.balance += amount
        return self.balance


    def withdraw(self, amount):
        # balance = balance - amount
        self.balance -= amount
        return self.balance


# instantiate the customer class as an object
mary = Customer('Mary', 836)
print (mary.name)
print ('Balance:', mary.balance)

current_balance = mary.deposit(208)
print(current_balance)
# print ('Current balance:', mary.balance)
# exit()
current_balance = mary.withdraw(492)
print(current_balance)
# print ('Current balance:', mary.balance)
# exit()


# we are creating a specific customer from the concept Customer
ella = Customer('Ella', 1167)
print(ella.name)
print('Balance:', ella.balance)

current_balance = ella.withdraw(503)
print(current_balance)
# print ('Current balance:', ella.balance)



class NumberManipulator:
    def __init__ (self):
        pass


    def addition(self, n1, n2):
        answer = n1 + n2
        return answer


    def subtraction(self, n1, n2):
        answer = n1 - n2
        return answer


    def multiplication(self, n1, n2):
        #answer = n1 * n2
        return n1 * n2


    def division(self, n1, n2):
        '''
        if n2 != 0:
            answer = n1 / n2
            return answer
        else:
            print ('***Cannot divide by 0***')
        '''
        try:
            answer = int(n1) / int(n2)
            return answer
        except:
            print ('***My abilities are limited young one! 134v3 m3 b3**')


    # Add concatenation '1, 1 = 11', '2, 7 = 27'
    def concatenation(self, n1, n2):
        answer = str(n1) + str(n2)
        return answer


n_m = NumberManipulator()
#Print returns of added functions
print('\n\nAdd- Number:', n_m.addition(738, 23))
print('Sub- Number:', n_m.subtraction(68, 927))
print('Multi- Number:', n_m.multiplication(87, 8))
print('Divi- Number:', n_m.division(70, 77))
#'2' means the number of decimal places
result = n_m.division(70, 77)
result = round(result, 2)
print (result)
#result = round(result, 0)
#print (result)
#print (type(result))
#print (int(result))
print ('Divi- Number:', n_m.division(1000, 0))
print ('Divi- Number:', n_m.division(500, 'uno'))
print ('Divi- Number:', n_m.division(250, '10'))
print('Con- Number:', n_m.concatenation(34, '65'))
exit()


class Friend:
    def __init__ (self, name_arg, age, nic_name, fav_colour, total = 0):
        self.name = name_arg
        self.age = age
        self.nicname = nic_name
        self.colour = fav_colour
        self.total = total


    def lend_moola(self, amount):
        self.total += amount

    #borrow moola()

#heyyyy.... soo, to me -0 is basically immortal as it's not a number and being immortal means you aren't affected by age, aka number. heh.. *nervous laugh
immortal = '-0'
jerry = Friend('Jerry', immortal, 'J', 'rainbow')
tom = Friend('Tom', immortal, 'T', 'Black & white')
print ('\n\nJerry\'s Total:', jerry.total)
jerry.lend_moola(7)
print ('Jerry\'s NEW Total:', jerry.total)
#Add properties e.g. name, nic-name, age, fav colour etc..
#Add both functions, lend money and money owe,d

# Test borrow_moola




# Create new class
class Pet():
    pass