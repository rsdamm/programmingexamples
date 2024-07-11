def main():
    find_primes()

def is_number(s):  #verify input is a number
    try:
        int(s)
        return True
    except ValueError:
        return False 
   
def find_primes():
    v_max_number=1
    
    # convert text to number
    v_text = input("Enter max range for prime numbers: ")
    if is_number(v_text):
        v_max_number = int(v_text)
    else: 
        print("Value entered was not a number")
        return
    print("printing prime numbers from 0 to " + v_text)

    j=0
    while (j <= v_max_number):

        v_not_a_prime = False
        i=2

        # see if number is prime  - must not have anything evenly divisible other that 1 and itself
        while (i < j): 
            x = j % i
            if x == 0: 
                v_not_a_prime = True
                break
            i+=1

        if v_not_a_prime == False:
            print(j) 
        j+=1
if __name__ == "__main__": 
    main()