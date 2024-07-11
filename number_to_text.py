def main():
    number_to_text()
def is_integer(p_number:str)-> bool:
    try:
        v_number = int(p_number)
        return True
    except TypeError:
        return False

def build_str_from_integer(p_int_input: str)-> str:

    v_tuples_text = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]  # to largest int 
    v_working_int_str = p_int_input
    v_word_equivalent = "" 
    v_hundreds = ""
    v_tens = ""
    v_ones = ""
    i = 0
    v_result = ""

    if v_working_int_str == "":
     return v_result 
    
    if v_working_int_str == "0":
        return "zero"
    if int(v_working_int_str) > 9999999999999999999:
        print ("Value greater than maximum value of 9999999999999999999")
        return ""
    
    # pad string with zeroes 

    while (len(v_working_int_str) % 3) != 0:
         v_working_int_str = "0" + v_working_int_str

    #loop through - converting the last 3 digits
    while len(v_working_int_str) > 0:

        v_word_equivalent = ""

        #get the last 3 digits
        v_hundreds = v_working_int_str[-3]
        v_tens = v_working_int_str[-2]
        v_ones = v_working_int_str[-1]

        print("H: " + v_hundreds + " T: " +  v_tens + " O: "+ v_ones)

        # get hundreds digit
        if v_hundreds != "0":
            v_word_equivalent = get_digit_word(v_hundreds) + " hundred" 

        if v_tens == "1":  # special case of teens
            if v_ones == "0":
                v_word_equivalent = v_word_equivalent + " ten"
            elif v_ones == "1":
                v_word_equivalent = v_word_equivalent + " eleven"  
            elif v_ones == "2":
                v_word_equivalent = v_word_equivalent + " twelve"  
            elif v_ones == "3":
                v_word_equivalent = v_word_equivalent + " thirteen"  
            elif v_ones == "4":
                v_word_equivalent = v_word_equivalent + " fourteen"  
            elif v_ones == "5":
                v_word_equivalent = v_word_equivalent + " fifteen"  
            elif v_ones == "6":
                v_word_equivalent = v_word_equivalent + " sixteen"  
            elif v_ones == "7":
                v_word_equivalent = v_word_equivalent + " seventeen"  
            elif v_ones == "8":
                v_word_equivalent = v_word_equivalent + " eighteen"  
            elif v_ones == "9":
                v_word_equivalent = v_word_equivalent + " nineteen" 

        if v_tens != "1":
            if v_tens == "2":
                v_word_equivalent = v_word_equivalent + " twenty" + " " + get_digit_word(v_ones) 
            elif v_tens == "3":
                v_word_equivalent = v_word_equivalent + " thirty" + " " + get_digit_word(v_ones) 
            elif v_tens == "4":
                v_word_equivalent = v_word_equivalent + " forty" + " " + get_digit_word(v_ones) 
            elif v_tens == "5":
                v_word_equivalent = v_word_equivalent + " fifty" + " " + get_digit_word(v_ones) 
            elif v_tens == "6":
                v_word_equivalent = v_word_equivalent + " sixty" + " " + get_digit_word(v_ones) 
            elif v_tens == "7":
                v_word_equivalent = v_word_equivalent + " seventy" + " " + get_digit_word(v_ones) 
            elif v_tens == "8":
                v_word_equivalent = v_word_equivalent + " eighty" + " " + get_digit_word(v_ones) 
            elif v_tens == "9":
                v_word_equivalent = v_word_equivalent + " ninety" + " " + get_digit_word(v_ones) 
            elif v_tens == "0":
                v_word_equivalent = v_word_equivalent + " " + get_digit_word(v_ones)


        # get tuple word
        v_word_equivalent = v_word_equivalent + " " + v_tuples_text[i] 
 
        #prep for next set of numbers
            
        v_result = v_word_equivalent + " " + v_result
        v_working_int_str = v_working_int_str [: -3]  # get all but the last 3 
        i += 1  # get next hundredths word

    #end while loop
        
    #clean up string
    v_result = " ".join(v_result.split())

    return (v_result)

def get_digit_word(p_digit: str) -> str:
    v_digit = p_digit
    v_word = ""

    if v_digit == "1":
        v_word ="one"
    if v_digit == "2":
        v_word ="two"
    if v_digit == "3":
        v_word ="three"    
    if v_digit == "4":
        v_word ="four"    
    if v_digit == "5":
        v_word ="five"    
    if v_digit == "6":
        v_word ="six"    
    if v_digit == "7":
        v_word ="seven"  
    if v_digit == "8":
        v_word ="eight"   
    if v_digit == "9":
        v_word ="nine"
    #if v_digit == "0":
    #    v_word = "" 
    return (v_word)
   
def number_to_text(): 

    v_result = ""
    
    #convert integer to text equivalent
    v_text = input("Enter an integer: ")
    if is_integer(v_text): 
        v_result = build_str_from_integer(v_text)
        print(str(v_text) + " = " + v_result)   
    else: 
        print("Value entered was not a number")

    return

if __name__ == "__main__": 
    main()