print("This program converts a decimal number to binary or hexadecimal.")
print(" ")
# Stores user's decimal number in a variable
bconNum = int(input("What is the decimal number you wish to convert to binary? "))
# Converts decimal to binary & removes the "b" in the return
binaryNum = bin(bconNum)
binaryNum = binaryNum.replace("b", "")
# Prints binary result
print(str(bconNum) + " in binary is: " + str(binaryNum))

# Stores user's decimal number in a variable
hconNum = int(input("What is the decimal number you wish to convert to hexadecimal? "))
# Converts decimal to hexadecimal
hexaNum = hex(hconNum)
# Prints hexadecimal result
print(str(hconNum) + " as a hexadecimal is: " + str(hexaNum))