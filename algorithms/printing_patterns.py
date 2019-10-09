'''
#rows
for i in range(0,5):
    #columns
    for j in range(0,i+1):
        print ('*', end ='')
    print ('\r')
'''


# half_pyramid() is a function that takes in the number of rows
def half_pyramid(num_r):
    #for each row -vertical
    for i in range(0,num_r):
        #for each column -horizontal
        for j in range(0,i+1):
            print ('*', end ='')
        print ('\r')

def tree_log(log_length,log_width):
    #for each row -vertical
    for i in range(0,log_length):
        #for each column -horizontal
        for j in range(0,log_width):
            print ('*',end ='')
        print ('\r')


half_pyramid(6)
half_pyramid(8)
half_pyramid(15)
half_pyramid(19)
tree_log(6,8)


'''

Extra fun!

1) Add a base to the tree - DONE! tree_log()
*
**
***
*
**
***
**** 
*****
*
*

2) Add "|" to the top of the tree
|
*
**
***
*
**
***
****

3) Add a star to the top of the tree
*
**
*
*
**
***
****
*****
*
**
***

4) Get the user to input the number of rows instead (hint: input())

5) Instead of a Christmas tree, let's make a ball instead
*
**
***
**
*

6) Let's make a snow man
*
**
*
*
**
***
****
*****
****
***
**
*

7) Use "/" and "\" instead of "*" - let's get creative!

8) Free style!

'''
