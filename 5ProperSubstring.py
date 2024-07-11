import array 
import random
import shlex

def main():
    v_strings = input("enter array of strings : ")
    print ("Input: ")
    print(v_strings)
    v_ok_string = check_proper_substring(v_strings)
    print ("Output: ")
    print (v_ok_string)

def check_proper_substring(p_strings)-> bool:    
    v_int = 0  
    v_ok = 0
 
    v_array = p_strings.strip('[] ').strip(' ').replace('"','').replace("'","").split(",")

    if len(v_array) < 2:
        return False
    
    v_nth_str = v_array[-1] 
    v_nth_minus_one = v_array[-2] 
 

    print("nth string: |" + v_nth_str + "|")
    print("nth-1 string: |" + v_nth_minus_one + "|")
    
    v_ok = v_nth_str.find(v_nth_minus_one)
    print (v_ok)

#bug only finds it if in the 1st position

    if v_ok == -1:
        return False
    
    return True

if __name__ == "__main__": 
    main()