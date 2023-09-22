# imports math library, which will be used to convert the decimal number to binary
import math
# the user input of what number they want to convert. Converts the input, which is a string, to an int. This will allow it to be used later for a math function
chosenNumber = int(input("Please enter your Binary. If nothing, put 0 "))
# converts the decimal number to binary and saves it in the variable binaryVersion
binaryVersion = bin(chosenNumber) 
# the bin function adds a random "b" in the binary number. The .replace() removes the b and saves the new value in binaryVersion1
binaryVersion1 = binaryVersion.replace("b", "")
# prints the given output, which changing the 
print("The binary of " + str(int(chosenNumber)) + " is " + str(binaryVersion1))