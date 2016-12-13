#GTIN challenge

# Initialise variables
gtinList = []

# Checks that the GTIN number entered is valid
while True:
        gtinNum = input("Please enter a 7 or 8 digit GTIN number!!")
        try: # Validation check to ensure the value entered is numeric.
                if int(gtinNum) and (6 < len(gtinNum) < 9 ):
                        gtinList = list(gtinNum)
                        break
        except ValueError: #If value entered is non-numeric then inform user
                print("GTIN should be numeric")
                print("Try again")
                
print("GTIN number entered is: ",gtinList)

# Counter to perform the main algorithm for task 1
calc = 0
for counter in range(0,7): # Loops from 0 upto, not including the 7th GTIN digit
        x = int(gtinList[counter]) 
        if (counter % 2) == 1:
            calc +=(x * 1)
        else:
            calc +=(x * 3)
print("Sum of GTIN7 digits is is: {}".format (calc))

# To calculate the nearest multiple of 10 I have used a counter
nearestTen = (calc + 9) // 10 * 10

print("Nearest multiple of 10 is: {}".format (nearestTen))

# Test to see if the eigth digit is present.
if len(gtinNum) == 8: # If GTIN num entered = 8 digits
        print("Validation check on eight digit of GTIN 8 number.")
        if (nearestTen - calc) == int(gtinNum[7]):
                print("GTIN8 checkDigit {} is valid".format (gtinNum[7]))
        else:
                print("GTIN8 checkDigit {} is not valid".format (gtinNum[7]))

