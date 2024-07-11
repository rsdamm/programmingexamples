import array 
import random

def main():
 
    v_bool = array_element_value_counter()
    print ("Output: ")
    print (v_bool)


def array_element_value_counter()-> bool:   
    v_number_of_entries = 0  
    v_array = []
    v_fifth_element = 0
    v_5_ctr = 0
    v_element = 0

    v_number_of_entries = int(input("Enter number of array entries : "))

    for i in range(0, v_number_of_entries):
        v_element = v_array.append(int(input()))
 
    if v_number_of_entries < 5:
        return False
    v_fifth_element = v_array[5]

    for i in range(v_number_of_entries):
        if v_array[i] == v_fifth_element:
            v_5_ctr +=1
 
    print ("Number of 5th element - " + str(v_fifth_element))
 
    if v_number_of_entries == 8 and v_5_ctr == 3:
        return True

    return False

if __name__ == "__main__": 
    main()