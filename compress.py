import zlib

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

def computable_info_density(np_array):
    byte_array = array_to_bytes(np_array)
    comp = zlib.compress(byte_array)
    return len(comp)/len(byte_array)
