x = 10

if x < 20:
    x = 25
    x = 26
    print(x + 10)
elif x == 20:
    x = 31
    if x != 40:
        print(x-1)
    else:
        print(x-2)
else:
    x = 30

# x = 10

# if x < 20:
#     x = 25
#     x = 26
#     if x == 10:
#         print(x+2)
# else:
#     x = 30

# print("XX")

# for i in range(1, 11):
#     x += 1
#     print(x-1)
#     if x == 10:
#         x = 11
#         print(x-34)
#     print(x+212)

# x = 0
# while x < 10:
#     x += 1

# print('done')

# x = 10

# i = 0
# while i < 20:
#     x += 1
#     if x + i % 2 == 0:
#         print('x + i is even')
#         for j in range (0, 11):
#             print('yay')
#         print('yays are done')
#     elif x + i % 5 == 0:
#         print('5s are okay')
#         for j in range(0, 3):
#             print('meh')
#     else:
#         print('ODDS')
#         print('oh no')
#     i += 1
#     print('this loop cycled')

# print('program over')
        

# print(x-2)
# print(x)

# print(x)

# # Get user input for taxable income
# income = float(input("Please Enter employee's annual taxable income ... CAD($) "))

# # Ensure user enters a positive value for taxable income
# while income < 0: 
#     income = float(input("Value must be positive. Please Enter employee's annual taxable income ... CAD($) "))
 
# # Calculate taxes and tax bracket
# if income >= 0 and income <= 33389.00:
#     # Multiply income by the tax percentage of the selected tax bracket
#     incomeTax = 0.108 * income
#     # Store the tax bracket info in a variable to print later
#     taxBracket = '10.80% [$0 ... $33,389.01)'
# elif income >= 33389.01 and income <= 72164.00:
#     incomeTax = 0.1275 * income
#     taxBracket = '12.75% [$33,389.01 ... $72,164.01)'
# # This else will occur when income is in the highest tax bracket
# else:
#     incomeTax = 0.174 * income
#     taxBracket = '17.40% [$72,164.01 ..)'
    
# # Print the income tax and tax bracket to the screen
# print(f"\nEmployee's provincial tax value: CAD($) {format(incomeTax, '.2f')}")
# print(f"Employee's provincial tax bracket : {taxBracket}")