import array 
import random

def main():
 
    v_bool = compare_int_values()
    print ("Output: ")
    print (v_bool)


def compare_int_values()-> bool:    
    v_int = 0

    v_int = int(input("enter integer : "))
    print ("Input: ")
    print (v_int)
 
    if v_int > 4**4 and v_int % 34 == 4:
        return True

    return False

if __name__ == "__main__": 
    main()