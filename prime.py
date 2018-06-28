import math 
import time


def prime(user_range):
    time1 =time.time()
    count = 0
    #checks each number under the input number starting from 2 (including input number)
    # 0 and 1 are not prime, no need to check
    for number in range (2,user_range+1):
        if(number%int(user_range/4)==0):
            print("quater marker")
        #set prime checking system
        is_prime =1
        #for each number under the square root of the checking number
        for factor in range (2,int(math.sqrt(number)+1),1):
            #check if the smaller number is a factor.
            if(number % factor == 0):
                is_prime = 0
                #use to check each non-prime number
                #print("The value of ",number," is divisable by",factor)
                break
        if(is_prime==1):
            #use to check each prime number
            #print("The value of ",number, " is a prime number.")
            count +=1
    else:
        print("The number of prime numbers found was:",count)
        time2 = time.time()
        dt = time2 - time1
        print(dt, " seconds taken")
prime(int(input()))