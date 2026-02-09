#Xenia and Bit Operations
#from operator import or_, xor
import sys

def ispow2(n): #doesn't work for n = 0.
    neg = n & (n-1)
    if neg == 0:
        return True
    else:
        return False

def build_seg_tree(n, a): #n is length of a. Tree will have high-level nodes from 1 to n-1, and array will start at n to 2n-1, for a total length of 2n.
    #Position 0 will be 0 and unused.
    tree = [0] * (n) #upper nodes of tree.
    tree.extend(a) #leaves of tree.
    #Build upper nodes. 
    ###