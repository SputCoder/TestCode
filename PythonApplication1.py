## Caibidil 1-4
# print
print('\n\n################\n\nCaibidil 1-4:\n\n')
print('Print to screen')

# JOIN STRINGS TOGETHER
message1 = "It's a good                   " # trims right of text
message2 = " book!"  # THIS IS ANOTHER STRING (TEXT)
age = 55
# A.1
message3 = "Happy "+ str(age) + "th Birthday"
###A.1 LINE ABOVE
#ADD TO MESSAGE SOME CODE USING A DOT TO STRIP WHITESPACE OR SPACES ON THE RIGHT HAND SIDE OF TEXT ONLY
message1 = message1.rstrip() # removes spaces from the right side of message1 which is "It's good        " spaces between good an quotation mark
message2 = message2.title() # makes the words starting letter start with capital letter
# ADD ONE MESSAGE TO ANOTHER  ( = APPEND ONE MESSAGE TO OTHER)... JUST USE THE PLUS (+) SYMBOL... HANDY :)
message = message1 + message2 # joins the 2 messages
message4 = message3

print('\n\nMessages: ')
print(message)
print(message4)

# CAN'T ADD NUMBERS AND TEXT TOGETHER IF NUMBER MUST CONVERT TO STRING SEE A.1 ABOVE USING THE "CAST" str(...)
# AS IN EXAMPLE str(age)   ( age = number str(age) = string... SO NOW CAN ADD AGE TO A STRING MESSAGE...

## 4
# MAKE A LIST OR ARRAY OF GOOD BANDS... :)
print('\n\n####\n4. Lists')

bands = ['Thin Lizzy','Guns n Roses','AC DC','Led Zeppelin','ZZ Top']
#bands.sort(reverse=True) # order in reverse Z to A

print('\n\n1. Print list ')
print(bands) # prints out list on screen

bands.sort() # order list A to Z   
print('\n\n2. Print sorted list ')
print(bands) # and print to show that is again sorted in alphabetially in order
# list should now be...
# bands = ['AC DC','Guns n Roses','Led Zeppelin','Thin Lizzy','ZZ Top']

# print only the first item in the list = AC DC  ... index = 0 for first item
print('\n\n3. Print first item in list ')
print('bands[0]... index starts a 0')
print(bands[0]) # output shows... AC DC
print('\n\n4. Print fourth item in list. Best band!! :) ')
print('band[3]... not 4 as first item index starts at 0... 0,1,2,3...')
print(bands[3]) # output shows fourth item is list as index starts at 0,1,2,3 .... and shows Thin Lizzy

print('\n\n5. Print entire list by looping through each item of the list using a FOR loop')
#  a ':' at end of for loop

for band in bands:    # it needs a 'colon' ( : ) at end of FOR statement or else causes error
    print(band)       # four spaces or TAB indented to that print is inside 'for loop'


# if typed say..
print('\n\n5.1 print not indented (tabbed)...')
print('\nPrint outside of FOR LOOP. Not necessarily what is wanted if want to print ALL items')
print('Only prints the last band in the list')
for band in bands:
    print('..') # print anything... just something here in the loop
print(band) # NO INDENTATION... OUTSIDE OF LOOP... MAYBE IN ERROR... MAYBE MEANT TO TAB TO INCLUDE IN FOR LOOP

print('\n\nZZ Top is the last band in the list.')
# the for loop would loop through all the list but the print is outside the for loop and then it would only
# print the last value of band which would be the last band in the list = 'ZZ Top'


# Caibidil 5. 
# if statements

print('\n\n################\n\nCaibidil 5.') # \n = just prints a new line
band = 'AC DC'
#band = 'bon jovi'

if band == 'AC DC':  # the if statement needs ':'
    print(band)
    print('They are a good band.')   
else: # as does the else...
    print('They are just ok.')

#if want to test see if it is ac dc but you have test lowercase but actual string is in uppercase try...

if band.lower() == 'ac dc':  # checks for lowercase only by adding .lower() to variable band
    print(band)
    print('They are a good band.')   

print('\n\n')

# IF YOU WANT TO CHECK THE ABOVE bands LIST AND CHECK IF THERE IS THE BAND 'Thin Lizzy' AND THEY LEAVE A COMMENT 
# AGAIN USE FOR LOOP TO LOOP THROUGH LIST AND ADD AN IF STATEMENT

for band in bands:    # it needs a 'colon' ( : ) at end of FOR statement or else causes error
    if band.lower() == 'thin lizzy':  # AGAIN NEED ' : '  # two equals sign is a test to check if equal  and ' != ' to test if NOT EQUAL 
        print(band)       # TAB again as is inside IF statement
        print('They are the best!')
    else:
        print('Not worthy of a comment :(')
print('For loop ended. All bands in list checked to see if any good.')

print('\n\n')
# IF AND ELSE ARE INDENTED ONE TAB ONLY AS BOTH ARE INSIDE THE FOR LOOP

# OR JUST...
for band in bands:    # it needs a 'colon' ( : ) at end of FOR statement or else causes error
    if band == 'Thin Lizzy':  # EXACTLY WHAT IS IN THE LIST THIS TIME... 'Thin Lizzy'
        print('They are the best!')
    else:
        print('Not worthy of a comment :(')
print('For loop ended. All bands in list checked to see if any good.')
print('The same result')


print('\n\nScroll to top to view all outputs!')