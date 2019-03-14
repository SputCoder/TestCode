## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

# CAN PASS A VALUE TO THE FUNCTION

# MAKE NEW function
def categorise_bands( band_name, band_type):  # **1 ... TWO PARAMETERS NOW... NOT JUST ONE
    print('Band name: ' + band_name)
    print('Type of music: '+ band_type)
    print('Routine in function done.\n') ## \n just new line
    

### NOW NEED TO CALL THE FUNCTION TO SEE IT WORKING...
categorise_bands('Thin Lizzy', 'Heavy Rock') # function is now called where a list is passed
categorise_bands('AC DC', 'Metal')


### BUT THE ORDER OF ARGUEMENT MATTERS FOR EACH OF THE PARAMTERS IN THE FUNCTION
## SAY. YOU PUT Heavy Rock followed by Thin Lizzy
## THEN YOU WOULD GET...


print('Below is deliberately done in error...parameter order wrong')
categorise_bands( 'Heavy Rock', 'Thin Lizzy')   # WRONG ORDER COMPARING TO **1.... ABOVE
print('The information in this is wrong. As the parameters ORDER passed to function is wrong.')

print('\n\nScroll to top to view all outputs!')