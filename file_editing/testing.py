print ('hello world')
with open ('text.txt', 'r') as file1, open ('text2.txt', 'w') as file2:
    for i in file1:
        print (i)
        #print (type(i))
        if i == 'LAVA':
            print(i)
            print (i.upper())
            file2.write(i.upper())
    #file2.write('pillow, plushie.. LAVA!!')
