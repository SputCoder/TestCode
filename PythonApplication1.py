
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
message = message3

print('Message: ')
print(message)

# CAN'T ADD NUMBERS AND TEXT TOGETHER IF NUMBER MUST CONVERT TO STRING SEE A.1 ABOVE USING THE "CAST" str(...)
# AS IN EXAMPLE str(age)   ( age = number str(age) = string... SO NOW CAN ADD AGE TO A STRING MESSAGE...

## 4
# MAKE A LIST OR ARRAY OF GOOD BANDS... :)
bands = ['Thin Lizzy','Guns n Roses','AC DC','Led Zeppelin','ZZ Top']
#bands.sort(reverse=True) # order in reverse Z to A

print('1. Print list ')
print(bands) # prints out list on screen

bands.sort() # order list A to Z   
print('2. Print sorted list ')
print(bands) # and print to show that is again sorted in alphabetially in order
# list should now be...
# bands = ['AC DC','Guns n Roses','Led Zeppelin','Thin Lizzy','ZZ Top']

# print only the first item in the list = AC DC  ... index = 0 for first item
print('3. Print first item in list ')
print(bands[0]) # output shows... AC DC
print('4. Print fourth item in list. Best band!! :) ')
print(bands[3]) # output shows fourth item is list as index starts at 0,1,2,3 .... and shows Thin Lizzy

print('5. Print entire list by looping through each item of the list using a FOR loop')
#  a ':' at end of for loop

for band in bands:    # it needs a 'colon' ( : ) at end of FOR statement or else causes error
    print(band)       # four spaces or TAB indented to that print is inside 'for loop'


# if typed say..
print('5.1 Print outside of for loop. Not necessarily what is wanted if want to print ALL items')
for band in bands:
    print() # print nothing... just something here in the loop
print(band) # NO INDENTATION... OUTSIDE OF LOOP... MAYBE IN ERROR... MAYBE MEANT TO TAB TO INCLUDE IN FOR LOOP

# the for loop would loop through all the list but the print is outside the for loop and then it would only
# print the last value of band which would be the last band in the list = 'ZZ Top'