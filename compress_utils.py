import numpy as np
# This file contains utility functions to be used by the compress.py script

def copy(data,start,end):

    length = len(data)-start

    ret_data = []

    for i in range(0,end-start):
            ret_data.append(data[start:len(data)][i%length])
            
    return ret_data
    
    
def lengthOfCommonSubseq(seq1,seq2):
    
    i = 0
    while i < len(seq1) and i < len(seq2):
        if not seq1[i] == seq2[i]:
            break
        i += 1
        
    return i
        
	
def longestPrefix(data,pos,win_size,pv_size):
    
    start = 0+(pos > win_size)*(pos - win_size)
    
    if pos+pv_size < len(data):
        end = pos+pv_size
    else:
        end = len(data)
        
    longest_start = start
    longest_len = 0
    
    i = start
    while i < pos:
        lcs = lengthOfCommonSubseq(data[i:end],data[pos:end])
        
        if lcs > longest_len:
            longest_len = lcs
            longest_start = abs(pos-i)
        
        i += 1
        
    return longest_start,longest_len


# takes in a array of 1s and 0s
# and creates a list of bytes
# that holds the info in bits
def array_to_bytes(np_array):
    no_bytes = np_array.size//8+1
    result = []
    for i in range(no_bytes):

        # splitting the sequence into 8 bit chunks
        slice = np_array[i*8:np.min([(i+1)*8,np_array.size])].astype(np.int)

        # padding the last byte if nescessary
        if slice.size < 8:
            slice = np.append(slice,(8-slice.size)*[False])

        result.append(int(''.join(slice.astype(str)),2))

    return bytes(result)

