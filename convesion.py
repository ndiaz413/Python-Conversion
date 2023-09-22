print("This program converts a decimal number to binary or hexadecimal.")
print(" ")
# Stores user's decimal number in a variable
bconNum = int(input("What is the decimal number you wish to convert to binary? "))
# Converts decimal to binary & removes the "b" in the return
binaryNum = bin(bconNum)
binaryNum = binaryNum.replace("b", "")
# Prints binary result
print("The binary of " + str(bconNum) + " is: " + str(binaryNum))

# Stores user's decimal number in a variable
hconNum = int(input("What is the decimal number you wish to convert to hexadecimal? "))
# Converts decimal to hexadecimal & removes the "x" in the return
hexaNum = hex(hconNum)
hexaNum = hexaNum.replace("x", "")
# Prints hexadecimal result
print("The hexadecimal of " + str(hconNum) + " is: " + str(hexaNum))