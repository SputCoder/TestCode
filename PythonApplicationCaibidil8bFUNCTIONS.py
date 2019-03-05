## Caibidil 8
# print
print('\n\n###\n\nCaibidil 8:\n\n')
print('functions...')

##  WANT A FUNCTION TO STORE SUBROUTINE THAT WANT TO CALL A FEW TIMES
## USE KEYWORD 'def' and call it a name AND TO END THIS FUNCTION LINE ADD A ':' AT END OF FIRST LINE
## NEED ROUND BRACKETS '()' AT END OF NAME TO LET IT KNOWN IT IS A FUNCTION
print('The function below:')

def printToScreen():
    print('Function that just prints this text.')
    print('Routine in function done.\n') ## \n just new line

## NOW MUST CALL THE FUNCTION OR ELSE NOTHING HAPPENS
## IT JUST STORES THE SUBROUTINE... AND WAITS IDLY UNTIL IS CALLED INTO ACTION
# 
#print('\n\nNo sign of the contents of function... yet...:)\n\n')
#
#printToScreen()   # now the function is calles and something shoul happen... 

#print('\n\nShould now see the that the function subroutine ran ok.')
#print('Great. :)')

#  NOW SAY IF YOU WANT TO CALL THE FUNCTION MORE THAN ONCE
# CAN PUT IT IN A for loop OR A while loop...
# ... say 4 times
print('\n\nFOR LOOP')
for x in range(0, 3):
    printToScreen()

####

### OR IN A WHILE LOOP
print('\n\nWHILE LOOP')
i = 0
while i < 4:
  printToScreen()
  i += 1  # or i = i + 1 to increment counter i




print('\n\nScroll to top to view all outputs!')