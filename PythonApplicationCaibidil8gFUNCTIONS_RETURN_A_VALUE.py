## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

# ADD A RETURN VALUE TO THE FUNCTION

def categorise_bands( band_name, band_type):  
    # CHANGED THE FUNCTION A BIT. PRINT NOT HERE.    
    # print('Band name: ' + band_name)
    # print('Type of music: '+ band_type)
    # print('Routine in function done.\n') ## \n just new line
    band_category = band_name + ' category is ' + band_type # added a space ' ' between band and type
    return(band_category) # GIVES A VALUE TO THE FUNCTION AND RETURNS IT WHEN CALLED
    

## FUNCTION RETURNING A VALUE

output = categorise_bands('Thin Lizzy', 'Heavy Rock') # THE FUNCTION IS CALLED
print(output) 


print('\n\nScroll to top to view all outputs!')