def triple_check(num_list):
    #raise an error if the list passed is not of nums only
    triple_numbers = []
    for num in num_list:
        if not isinstance(num, int):
            raise TypeError('List must contain numbers only.')
        else:
            if num_list.count(num) >= 3:
                triple_numbers.append(num)
        
    remaining = [num for num in num_list if num not in triple_numbers]
    #convert remaining into  a single int
    
    return tuple(remaining)






    