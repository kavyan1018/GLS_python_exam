"""

        if(){
            
        }else{
            
        }


    if condition :
        # code 
    else :
        # code    
"""

# no1 =  10

# if no1 > 0 :
#     print("Positive Number")
# else :
#     print("Negative Number")
    
    
     
"""   
    # else if 
    
    if condition1 :
        # code
    elif condition2 :
        # code
    else :
        # code

"""

# a = int(input("Enter a First Numebr : "))
# b = int(input("Enter a Second Number : "))
# c = int(input("Enter a Third Number : "))


# if a > b and a > c :
#     print("A is Greater")
# elif b > a and b > c :
#     print("B is Greater")
# else :
#     print("C is Greater")


# Nested if else

age = input("Enter Your Age : ")

if int(age) >= 18 :
    
    id = input("Do You Have Voter ID (Yes/No) : ")
    if id == "Yes" or id == "yes" or id == "YES" :
        print("You are Eligible for Voting")
    else :
        print("You Dont have Voter ID, So You are Not Eligible for Voting")
else : 
    print("You are Under Age, So You are Not Eligible for Voting")