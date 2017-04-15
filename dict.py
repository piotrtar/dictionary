import csv
import time


with open('file.csv', 'r') as f:    
    reader = csv.reader(f)              #The reader function is designed to take each line of the file and make a list of all columns
    dic = dict(reader)                  #importing data from file.csv to dic(ionary) which is created

working = True
while working:
    print("<<<<Dictionary for a little programmer:>>>>\n")
    print("1) search explanation by appellation")
    print("2) add new definition")
    print("3) show all appellations alphabetically")
    print("0) exit")
    

    number = input("Enter a number: ")

    if number == '1':
        print("Wirte a appellation: ")
        appellation = input().lower()   #inputting searching word
        if dic.get(appellation):        #checking if file contains that word
            print (dic[appellation])
        else:
            print("Appellation not known. You can create one or look for another one!")

    elif number == '2':
        print ('Enter a new appellation: ')
        new_app = input().lower()                   #inputting new appellation
        while len(new_app) < 1:                     #repeat if pressed enter instead of putting anything
            print("No word was given. Try again.")
            print ('Enter a new appellation: ')
            new_app = input().lower() 
        
        print ('Enter a new definition: ')
        new_def = input().lower()                   #inputting definition
        while len(new_def) < 1:
            print("Now word was given. Try again.")
            print ('Enter definition of definition: ')
            new_def = input()

        print ('Enter a source of definition: ')
        new_s = input()                             #inputting source
        while len(new_s) < 1:
            print("No source was given. Try again.")
            print('Enter a source of definition: ')
            new_s = input()

        dic[new_app] = (new_def , new_s)            #adding new appelation to dictionary, respectively definition and source
        with open('file.csv', 'w') as f:            #opening file to write it     
            writer = csv.writer(f)
            for word, tupl in dic.items():          #for 1st and 2nd elemenent in items in dictionary
                writer.writerow([word, tupl])       #write them in new row respectively word and tup1 it is definition and source
        print("New appellation added successfuly")

    elif number == '3':
        for i in sorted(dic.items()):               #to sort dictionary alphabetically
            print(i[0])                             #print 1st elements it is appellations

    elif number == '0':
        print("Thank you! Goodbye!")
        working = False
    else:
        print(">>>>Enter only number from 0 to 3!<<<<\n")
        time.sleep(1.5)

  

