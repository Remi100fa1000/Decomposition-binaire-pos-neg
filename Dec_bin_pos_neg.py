# In this file, we decompose an integer as the sum of powers of two.
# Compared to the traditional binary decomposition, we decompose the number in
# positive and negative  numbers
# So as to reduce the number of factors.
# For example, 7 is decomposed as 8-1 instead of 1+2+4
#
# Remi100fa1000

# As input we have an integer,
# As output we have the array which contains the list of powers of two whose sum
# is equal to Myinteger
def Dec_bin_pos_neg(Myinteger):
    Myint                       = Myinteger

    # Our result
    Result                      = []

    while(Myint!=0):

        Mybinary               = bin(Myint) # We write the binary decomposition of the integer
        
        if(Myint>0):
            MSB_index              = len(Mybinary)-2 # The binary decomposition gives a string, the MSB is given at index at index len()-2
            
            # We have two choices, we can either remove 2^MSB-1 or 2^MSB from our integer 
            # In this second case, the new integer obtained is negative.
            # We choose to have the smallest number (absolute value)
            if(abs(Myint-(2**(MSB_index-1)))<abs(Myint-(2**(MSB_index)))):
                Result.append(2**(MSB_index-1))
                Myint              = Myint-2**(MSB_index-1)
            else:
                Result.append(2**(MSB_index))
                Myint              = Myint-2**(MSB_index)
        # In the case where our integer is negative, instead of removing the power of two, we add it
        else:
            MSB_index              = len(Mybinary)-3 #We have a minus one in the binary representation
            
            if(abs(Myint+(2**(MSB_index-1)))<abs(Myint+(2**(MSB_index)))):
                Result.append(-2**(MSB_index-1))
                Myint              = Myint+2**(MSB_index-1) #In this case, the number stays negative
            else:
                Result.append(-2**(MSB_index))
                Myint              = Myint+2**(MSB_index) # In this case, the new number is positive

    return Result


#Some example results
print(Dec_bin_pos_neg(7))
print(Dec_bin_pos_neg(-7))
print(Dec_bin_pos_neg(127))
print(Dec_bin_pos_neg(1023))
