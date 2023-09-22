# Stores user's decimal number in a variable
conversionNum = int(input("What is the decimal number you wish to convert to binary? "))
# Uses the bin() function to convert the decimal to binary
binaryNum = print(bin(conversionNum))
binaryNum = binaryNum.replace("b", "")
