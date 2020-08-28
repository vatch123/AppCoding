import numpy as np

def bernouli_erasure(erasure_prob):
    
    x = np.random.uniform()
    return True if x < erasure_prob else False


def gilbert_elliot_erasure(previous_status, erasure_prob1, erasure_prob2):

    # Check if packet_number-1 was lost
    if previous_status:
        x = np.random.uniform()
        return True if x < erasure_prob1 else False
    
    else:
        x = np.random.uniform()
        return True if x < erasure_prob2 else False

