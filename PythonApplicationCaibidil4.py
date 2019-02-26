## Caibidil 4
# print
print('\n\n################\n\nCaibidil 4:\n\n')
print('Print to screen')

## 4
# MAKE A LIST OR ARRAY OF GOOD BANDS... :)

bands = ['Thin Lizzy','Guns n Roses','AC DC','Led Zeppelin','ZZ Top']
#bands.sort(reverse=True) # order in reverse Z to A

print('\n\n1. Print list ')
print(bands) # prints out list on screen
bands.sort() # order list A to Z   


print(bands)
# list should now be...
# bands = ['AC DC','Guns n Roses','Led Zeppelin','Thin Lizzy','ZZ Top']

# print only the first item in the list = AC DC  ... index = 0 for first item
print('\n\n3. Print first item in list ')
print('bands[0]... index starts a 0')
print(bands[0]) # output shows... AC DC

print('\n\n4. Print fourth item in list. Best band!! :) ')
print('band[3]... not 4 as first item index starts at 0... 0,1,2,3...')
print(bands[3]) # output shows fourth item is list as index starts at 0,1,2,3 .... and shows Thin Lizzy


# FOR LOOP EXAMPLE WITH LISTS

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
