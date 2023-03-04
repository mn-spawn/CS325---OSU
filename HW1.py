import sys
import time
# Usage when run from the command line: python max_subarray_homework1.py 
#<filename>.
# Example usage:                        python max_subarray_homework1.py 
#num_array_500.txt
file_name = sys.argv[1]
f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

#to run:
#python mspawn_cs325_hw1.py 
#or
#python3 mspawn_cs325_hw1.py



def max_subarray_enumeration(A):
    if not A: return 0    

    max = -sys.maxsize
    size = len(A)
    for i in range(size):
        for j in range(i, size):
            temp = 0
            for k in range(i, j+1):
                temp += A[k]
                if temp > max:
                    max = temp
    return max


def max_subarray_iteration(A):
    if not A: return 0  
        
    max = -sys.maxsize-1
    size = len(A)
    for i in range(size):
        current = 0
        for j in range(i, size):
            current += A[j]
            if current > max:
                max = current
    return max




def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times 
how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute 
alg(A) in milliseconds.
    """
    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time
for alg in [max_subarray_enumeration, max_subarray_iteration]:
    print(file_name, time_alg(alg, A))