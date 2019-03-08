## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

# CAN PASS A VALUE TO THE FUNCTION
# BUT CAN ALSO PASS A LIST (MORE THAN ONE VALUE) INSIDE THE ROUND BRACKETS
print('The function below:\n')

#username = 'Thin Lizzy' # a varible declared and initialized as a string
# BACK TO OUR LIST CALLED bands
bands = ['Thin Lizzy','Guns n Roses','AC DC','Led Zeppelin','ZZ Top']

# PASS THIS LIST... bands
def printToScreen(bands):  # bands list is the values being passed
    # ADD for LOOP TO PRINT EACH BAND ONE BY ONE
    for band in bands:    # it needs a 'colon' ( : ) at end of FOR statement or else causes error
        print(band)       # four spaces or TAB indented to that print is inside 'for loop'
 
    print('Routine in function done.\n') ## \n just new line
    # this print statement only prints out once as it is not tabbed in for the FOR loop
    # but IS.... IN LINE with the FOR LOOP 
    # and TABBED within the def (or function)... so OPERATES INSIDE the function

### NOW NEED TO CALL THE FUNCTION TO SEE IT WORKING...
printToScreen(bands) # function is now called where a list is passed

print('\nYeah... and we should have our list of bands printed out')

print('\n\nScroll to top to view all outputs!')