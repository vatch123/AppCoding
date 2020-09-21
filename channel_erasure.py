import random

def bernouli_erasure(success_prob):
    """
    Probability that the message will be sucessfully
    """
    
    x = random.uniform(0,1)
    return True if x < success_prob else False


def gilbert_elliot_erasure(previous_status, Pbg, Pgb):
    """
    Previous state
    Pbg: Probability of transition from bad to good.
    Pgb: Probability of transition from good to bad
    """

    # Check if packet_number-1 was lost
    if not previous_status:
        x = random.uniform(0,1)
        return True if x < Pbg else False
    
    else:
        x = random.uniform(0,1)
        return True if x < 1 - Pgb else False

