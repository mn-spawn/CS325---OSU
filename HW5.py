import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2, ci = 1, cd = 1, cm = 1):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        ci: The cost of an insertion (1 by default).
        cd: The cost of a deletion (1 by default).
        cm: The cost of a mutation (1 by default).
    
    Returns:
        The edit distance between s1 and s2.
    """

    # this function implements a tabulation approach
    #init the tbale with 0's so we can fill in
    T = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]


    #here we start filling in the table
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):

            #if first row or column it is 0
            if i == 0:
              T[i][j] = 0  

            if j == 0:
             T[i][j] = 0


            else:
                #we have three cases here
                #get the cost of 
                insert = T[i][j-1] + ci
                #get cost of deletiong by looking 
                delete = T[i-1][j] + cd
                #
                sub = T[i-1][j-1] + (cm if s1[i-1] != s2[j-1] else 0)

                #we want to do the min change
                T[i][j] = min(insert, delete, sub)


    #return final cell of table
    return T[len(s1)][len(s2)]
    
def lcs(s1, s2):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """

    #more tabulation

    # Initialize the table with zeros.
    table = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # fill in the table using dynamic programming.
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                
                #we got a match? cool add it to the tally update the table
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                #no match? get the previously calculated max
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    # Return the length of the LCS
    #not the length so that the table starts at 0 and we don't go out of bounds if
    #we need data in the very beggining of filling out the table

    return table[-1][-1]
    


def lcs3(s1, s2, s3):
    """
    Computes the length of the longest common subsequence between three strings: s1, s2, and s3.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The third string.
    
    Returns:
        The length of the longest common subsequence between s1, s2, and s3.
    """
    #surprise this code is pretty much the exact same as above!
    #now we just have three loops compare three strings and return three idices
    #structure is exaxt same though

    table = [[[0 for _ in range(len(s3)+1)] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    #fill in the table using dynamic programming

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            for k in range(1, len(s3)+1):
                if s1[i-1] == s2[j-1] == s3[k-1]:
                    table[i][j][k] = table[i-1][j-1][k-1] + 1
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
    

    #not the length so that the table starts at 0 and we don't go out of bounds if
    #we need data in the very beggining of filling out the table
    return table[-1][-1][-1]


s1 = file_contents_letters(sys.argv[1])
s2 = file_contents_letters(sys.argv[2])
print(edit_distance(s1, s2), lcs(s1, s2))

#for me to copy and paste into terminal
# python3 HW5.py COVID-RefDec19.txt COVID-OmicronBA1.txt
