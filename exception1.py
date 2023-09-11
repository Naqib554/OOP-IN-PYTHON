def make_list_of_ones(length):
    if length<=0:
        # raising exception
        raise ValueError("Invalid length") # will stop the programe and raise an error
    return [1]*length

make_list_of_ones(-1)

# it is the way to handle error correctly 
# This allows your program to continue running or provide a more user-friendly error message.
     
    