import sys
import time

# Usage when run from the command line: python max_subarray_homework1.py <filename>.
# Example usage:                        python max_subarray_homework1.py num_array_500.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def maxRecArray(A, start, end):
    #invalid array
    if not A:
        return 0
    #base case
    if start == end:
        return A[start]

    middle = (start+end) // 2

    #three cases

    #prefix (left)
    prefMax = -sys.maxsize
    sumArray = 0
    for i in range(middle, start-1, -1):
        sumArray += A[i]
        #if the current array calculated is greater than prev greates update
        if sumArray > prefMax:
            prefMax = sumArray

    #suffix (right)
    sufMax = -sys.maxsize
    sumArray = 0
    for i in range(middle+1, end+1):
        sumArray += A[i]
        #if the current array calculated is greater than prev greates update
        if sumArray > sufMax:
            sufMax = sumArray

    maxSide = max(sufMax, prefMax)
    #crossing array
    return max(maxSide, (sufMax + prefMax)) 



def max_subarray_simplification_delegation(A):
   return maxRecArray(A, 0, len(A)-1)


def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in milliseconds.
    """

    start_time = time.monotonic_ns() // (10 ** 6) # The start time in milliseconds.
    max_subarray_val = alg(A)
    end_time   = time.monotonic_ns() // (10 ** 6) # The end time in milliseconds.
    return max_subarray_val, end_time - start_time

for alg in [max_subarray_simplification_delegation]:
    print(file_name, time_alg(alg, A))


#

