
import heapq # Hint: use Python's priority queue class, heapq.
import sys

class Node:
    def __init__(self, count, children):
        self.count    = count
        self.children = children
        
    def is_leaf(self):
        return False
        
    def __lt__(self, other):
        return self.count < other.count
    def __eq__(self, other):
        return self.count == other.count
    def printNode(self):
        print("count: ", self.count)
        print("children: ", self.children)
        
        
class LeafNode(Node):
    def __init__(self, symbol, count):
        super().__init__(count, [])
        self.symbol = symbol
        
    def is_leaf(self):
        return True

    def printNode(self):
        print("count: ", self.count)
        print("symbol: ", self.symbol)

def recursiveBinaryCode(n, binString, d, HMCode):
    if n.is_leaf():
        d[n.symbol] = binString
        HMCode.C = d
        return
    else:
        recursiveBinaryCode(n.children[0], binString+'0', d, HMCode)
        recursiveBinaryCode(n.children[1], binString+'1', d, HMCode)

class HuffmanCode:
    def __init__(self, F):
        self.C = dict()
        self.T = None
        self.cost = 0 
        self.average_cost = 0
        self.F = F
        # TODO: Construct the Huffman Code and set C, T, cost, and average_cost properly!


    def encode(self, m):
            """
            Uses self.C to encode a binary message.   
            Parameters:
                m: A plaintext message.

            Returns:
                The binary encoding of the plaintext message obtained using self.C.
            """
            Q = []
            F = get_frequencies(m)
            Flist = list(F.items())


            for sub in Flist:
                newNode = LeafNode(sub[0], sub[1])
                heapq.heappush(Q,newNode)
                
            heapq.heapify(Q)

            for j in range(len(Q)-1):
                #children - left then right
                if(len(Q) != 0):
                    left = heapq.heappop(Q)
                if(len(Q) != 0):
                    right = heapq.heappop(Q)
                count = (left.count + right.count)

                newN = Node(count, [left, right])
                
                heapq.heappush(Q,newN)

            nodeHead = heapq.heappop(Q)

            recursiveBinaryCode(nodeHead, "", F, self)

            st = ""
            for i in range(0, len(m)):
                st += self.C.get(m[i])
   
            return st
            
    def decode(self, c):
            """
            Uses self.T to decode a binary message c = encode(m).
    .    
            Parameters:
                c: A message encoded in binary using self.encode.
            
            Returns:
                The original plaintext message m decoded using self.T.
            """
            x = list(self.C.items())
            str = ''
            str2 = ''
            for i in range(0, len(c)):
                for j in range(len(x)):
                    if x[j][1] == str:
                        str = ''
                        str2 += x[j][0]
                else:
                    str += c[i]

            return str2
        
    def get_cost(self):
        """
        Returns the cost of the Huffman code as defined in CLRS Equation 16.4.
            
        Returns:
        Returns the cost of the Huffman code.
            """ 
        sum = 0
        x = list(self.F.items())
        y = list(self.C.items())

        for i in range(len(x)):
            sum+= (len(y[i][1]) * (x[i][1]))
            
        self.cost = sum

        return self.cost
        
    def get_average_cost(self):
        """
        Returns the average cost of the Huffman code.
        
        Returns:
            Returns the average cost of the Huffman code.
        """ 
        sum = 0
        x = list(self.F.items())
        for i in range(len(x)):
            sum += x[i][1]
        self.average_cost = self.cost/sum
        return self.average_cost
        
def get_frequencies(s):
    """
    Computes a frequency table for the input string "s".
    
    Parameters:
        s: A string.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in s).
    """
    F = dict()
    
    for char in s:
        if not(char in F):
            F[char] = 1
        else:
            F[char] += 1
            
    return F
    
def get_frequencies_from_file(file_name):
    """
    Computes a frequency table from the text in file_name.
    
    Parameters:
        file_name: The name of a text file.
        
    Returns:
        A frequency table F such that F[c] = (# of occurrences of c in the contents
of <file_name>).
    """
    f = open(file_name, "r")
    s = f.read()
    f.close()
    return get_frequencies(s)

if __name__ == "__main__":
    HC = HuffmanCode(get_frequencies_from_file("gba.txt"))
    HC.decode(HC.encode())
    print(HC.get_cost())