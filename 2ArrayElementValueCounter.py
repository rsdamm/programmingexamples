import array 
import random

def main():
 
    v_bool = array_element_value_counter()
    print ("Output: ")
    print (v_bool)

def array_element_value_counter()-> bool:
    v_5_ctr = 0
    v_19_ctr = 0 
    v_number_of_elements = 8
    v_max_value = 20
    v_min_value = 0

    v_array = random.sample(range(v_min_value, v_max_value), v_number_of_elements) 
    print(v_array)  

    #loop through - counting
    for i in range( len(v_array)):
        if v_array[i] == 5:
            v_5_ctr +=1

        if v_array[i] == 19:
            v_19_ctr +=1
    if v_19_ctr == 2 and v_5_ctr == 3:
        return True

    return False

if __name__ == "__main__": 
    main()