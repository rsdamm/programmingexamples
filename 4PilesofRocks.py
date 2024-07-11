import array 
import random

def main():
 
    build_piles()

def build_piles():    
    v_int = 0
    v_current_pile_ct = 0
    v_array = []

    v_int = int(input("enter number of piles : ")) 
    print ("Input: ")
    print (v_int)

    v_current_pile_ct = v_int 
    
    for i in range(v_int): 
        v_array.append(v_current_pile_ct) 
        v_current_pile_ct = v_current_pile_ct + 2
 
    print ("Output: ")
    print (v_array)

    return 

if __name__ == "__main__": 
    main()