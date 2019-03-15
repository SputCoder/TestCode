## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

#################
######
###### THIS PROGRAM NEEDS THE ADDITIONAL FILE function_testing_module.py 
###### TO WORK PROPERLY 
###### THE PROGRAM NEEDS TO IMPORT CONTENTS OF THAT FILE... :)

# CAN STORE FUNCTIONS IN A SEPARATE FILE WHICH IS A MODULE
# AND CAN GRAB IT BY USING import

import function_testing_module  # imports module that has functions
## when naming a module/file that stores functions
## must use _ (underscore) and not - (dash) or else get an error

## OK, THE FUNCTION IS IMPORTED SO IT NOW CAN BE USED
## BUT, TO USE THE FUNCTION MUST IDENTIFY WHICH MODULE IT IS
## WHEN CALLING THE FUNCTION [stored on a separate file]


## FUNCTION RETURNING A DICTIONARY
# output = categorise_bands('Thin Lizzy', 'Heavy Rock') # THE FUNCTION IS CALLED

## MUST CHANGE FUNCTION TO...
output = function_testing_module.categorise_bands('Thin Lizzy', 'Heavy Rock')

# NEED TO ADD functions-testing-module. TO FUNCTION 
print('\nIMPORTING THE ENTIRE MODULES... THAT COULD HAVE MANY FUNCTIONS')
print(output) # output is in the form of a dictionary... like a list

###  CAN IMPORT JUST ONE FUNCTION THAT YOU REQUIRE
### RATHER THAN IMPORTING THE WHOLE MODULE THAT MIGHT HAVE MANY FUNCTIONS

print('\nIMPORTING ONLY ONE FUNCTION')
from function_testing_module import categorise_bands
output2 = categorise_bands('Thin Lizzy', 'Heavy Rock')

### NOW DON'T NEED TO SPECIFY WHICH MODULUE JUST USE FUNCTION AS BEFORE

# NEED TO ADD functions-testing-module. TO FUNCTION 

print(output2) # output is in the form of a dictionary... like a list
print('It is the same outcome.')


######## NOTES

## AND IF WANT TO IMORT ALL FUNCTIONS FROM A MODULE THEN CAN USE
### from function_testing_module import *   ## use the * ... for all
## and can use output3 = categorise_bands('Thin Lizzy', 'Heavy Rock')
### no need for 'function_testing_module.'cate...... when calling a function



## can also use an alias for a module if you need to use module name in the function
## say,   import function_testing_module as ftm


## or can use an alias for a function even
## from function_testing_module import categorise_bands as cb
## and use like the following: 
## output4 = cb('Thin Lizzy', 'Heavy Rock')




print('\n\nScroll to top to view all outputs, if there are many!')


