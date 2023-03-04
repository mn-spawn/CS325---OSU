import sys
import time
# Usage when run from the command line: python max_subarray_algs.py <filename>.
# Example usage:                        python max_subarray_algs.py 

file_name = sys.argv[1]
f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def max_subarray_recursion_inversion(A):
    """
    Computes the value of a maximum subarray of the input array by "recursion 
inversion" (i.e., dynamic programming).
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    #set an overall and then compute the maximum for each calculated array
    #set this equal to the minimum integer incase we get a negative number to start or result
    overallmax = -sys.maxsize-1
    length = len(A)

    #according to the "recursion inversion" slide we want to calculate and store each preceding
    #max subarray and then use that to calculate future max subarrays

    overallmax = A[0]
    maxCurrSum = A[0]
    for i in range(1, length):

            #we update the overall max based on the what is bigger the value before (without adding the next val)
            #this is the base of the logic of DP...we calculate things in a kind of cinammon roll fashion
            #each layer builds on the previous one to efficiently compute the problem
            overallmax = max(A[i], overallmax + A[i])
            maxCurrSum = max(maxCurrSum, overallmax)


    return overallmax
  
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
for alg in [max_subarray_recursion_inversion]:
    print(file_name, time_alg(alg, A))