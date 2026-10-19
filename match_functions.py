"""

    switch(choice){
     
        case 1:
            // code
            break;
        
        case 2:
            // code
            break;

        case 2:
            // code
            break;
        
        default:
            // code
            break;
        
    }
    
    
    
    match choice:
        case 1:
            # code
            break
        case 2:
            # code
            break
        case 3:
            # code
            break
"""


choice = int(input("Enter the Numebr between 1 to 7 to print the day : "))

match choice:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
