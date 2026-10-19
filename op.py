# Arithmetic op
# bitwise op
# Assign op
# relational op
# logical op
# math op
# Unary op
# identity op
# boolean op
# membership op


# Arithmetic op 
'''
    + -> addition
    - -> subtraction
    * -> multiplication
    / -> division
    % -> modulus
    ** -> exponentiation
    // -> floor division
'''


# a = 10
# b = 3


# print("Addition :", a + b)
# print("Subtraction :", a - b)
# print("Multiplication :", a * b)
# print("Division :", a / b)
# print("Modulas :", a % b)
# print("Floor Division :", a // b)
# print("Exponentation :", a ** b)



# bitwise op
'''
    & -> bitwise AND
    or -> bitwise OR
    ^ -> bitwise XOR
    not -> bitwise NOT ~
'''


# a = 5
# b = 3

# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~a)
# print(~b)


# Assignment op
'''

    = -> assign 
    += -> add and assign
    -= -> subtract and assign
    *= -> multiply and assign
    /= -> divide and assign
    %= -> modulus and assign
    **= -> exponentiation and assign
    //= -> floor division and assign   

'''


# a = 10
# a += 5    # a = a + 5
# print(a)   # 15

# a -= 4   # 15 - 4 = 11
# print(a)

# a *= 2  # a = a * 2  -> 10 * 2 = 20  a = 20
# print(a)  

# a /= 5      # a = a / 5  -> 20 / 5 = 4.0
# print(a)


# a %= 3
# print(a) 

# a **= 2
# print(a)

# a //= 3
# print(a)  


# Relational op

'''
    == -> equal to
    != -> not equal to
    > -> greater than
    < -> less than
    >= -> greater than or equal to
    <= -> less than or equal to
    << -> left shift
    >> -> right shift
'''

# a = 10
# b = 20

# print(a == b)   
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# print(a << 3)   # 10 << 2 -> 
"""
    10 -> 101000
"""

# print(a >> 2)   


# Logical op

"""
    and 
    or
    not 
"""

# a = 1
# print(a > 5 and a < 30)
# print(a > 5 or a < 30)
# print(not(a > 5))   # 1 > 5


# identity op     -> it check the two variables are pointing to the same object or not

# a = [10, 20]
# b = a
# c = [10, 20]

# print(a is b)
# print(b is c)
# print(a is not c)


# boolean op

# True and False

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)