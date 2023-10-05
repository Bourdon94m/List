


def append_list():


    # user var 
    turn = input("How many number would you add on this list ? : ") #We ask the user how many number he want on the list
   


    # empty list 
    my_list = []

    
    # boucle for in range of {turn} var
    for i in range(int(turn)):

        user_input_list = input("Enter a value and we add it to the list : ") #We ask the user to enter the number of his choice
        int_user_input_list = int(user_input_list) #convert it in integer
        


        
        my_list.append(int_user_input_list) # This var append the {int user input list} in {my list}


        # min and max in {my_list}    
        min_on_list = min(my_list)
        max_on_list = max(my_list)


    print(f"on {my_list}, the minimum is {min_on_list}, and the maximum of this list is {max_on_list}")



append_list()