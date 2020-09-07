import numpy as np

def bernouli_erasure(erasure_prob):
    
    x = np.random.uniform()
    return True if x < erasure_prob else False


def gilbert_elliot_erasure(previous_status, Pbg, Pgb):
    """
    Previous state
    Pbg: Probability of transition from bad to good.
    Pgb: Probability of transition from good to bad
    """

    # Check if packet_number-1 was lost
    if previous_status:
        x = np.random.uniform()
        return True if x < Pbg else False
    
    else:
        x = np.random.uniform()
        return True if x < 1 - Pgb else False

