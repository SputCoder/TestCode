## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

# ADD A RETURN VALUE TO THE FUNCTION

def categorise_bands( band_name, band_type):  
    band_category = { 'name': band_name, 'type': band_type }  # this is the form of a DICTIONARY... it's like a list or array
    return(band_category) # GIVES A VALUE TO THE FUNCTION AND RETURNS IT WHEN CALLED

## FUNCTION RETURNING A DICTIONARY
output = categorise_bands('Thin Lizzy', 'Heavy Rock') # THE FUNCTION IS CALLED
print(output) # output is in the form of a dictionary... like a list


print('\n\nScroll to top to view all outputs, if there are many!')
